from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from requests import request
from django.contrib.auth.decorators import login_required
from restaurant.forms import CheckoutForm, ContactForm, BlogReviewForm
from .models import *
from django.db.models import Q


# Create your views here.
# Login Required View for all views
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls):
        return login_required(super(LoginRequiredMixin, cls).as_view())

class IndexView(generic.ListView):
    template_name = 'homepage/index.html'
    def get(self, request, *args, **kwargs):
        food_category_id = self.kwargs.get('food_category_id')
        food_category_list = FoodCategory.objects.all().order_by('-food_category_id')[:4]
        restaurant_id = self.kwargs.get('restaurant_id')
        restaurant_obj = Restaurant.objects.all().order_by('-restaurant_id')[:4]
        food_id = self.kwargs.get('food_id')
        food_obj = Food.objects.all().order_by('-food_id')[:4]
        context = {
            'food_category_list' : food_category_list,
            'restaurant_obj' : restaurant_obj,
            'food_obj' : food_obj,
        }
        return render(request, self.template_name, context)

class RestaurantView(generic.ListView):
    def get(self, request, *args, **kwargs):
        template_name = "restaurant/restaurant.html"
        restaurants_list = Restaurant.objects.all()
        context = {
            'restaurants_list': restaurants_list
        }
        return render(request, template_name, context)

class RestaurantDetailView(generic.DetailView):
    def get(self, request, *args, **kwargs):
        template_name = "restaurant/resto_detail.html"
        restaurant_detail_list = Restaurant.objects.get(restaurant_id=self.kwargs.get('restaurant_id'))
        categories = FoodCategory.objects.all()
        context = {
            'restaurant_detail_list': restaurant_detail_list,
            'categories' : categories,
        }
        return render(request, template_name, context)
 
class FoodView(generic.ListView):
    template_name = "foods/food.html"
    def get(self, request, *args, **kwargs):
        food_id = self.kwargs.get('food_id')
        food_obj = Food.objects.all().order_by('-food_id')
        food_category_id = self.kwargs.get('food_category_id')
        food_category_obj = FoodCategory.objects.all().order_by('-food_category_id')
        print(food_category_obj)
        context = {
            'food_obj': food_obj,
            'food_category_obj' : food_category_obj,
        }
        return render(request, self.template_name, context)

class FoodDetailView(generic.DetailView):
    template_name = "foods/detail.html"
    def get(self, request, *args, **kwargs):
        food_id = self.kwargs.get('food_id')
        food_detail_obj = Food.objects.get(food_id = food_id)
        return render(request, self.template_name, {'food_detail_obj': food_detail_obj})

class AddToCartView(generic.TemplateView):
    template_name = 'homepage/addtocart.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        # get food id from requested url
        food_id = self.kwargs['fd_id']
        # get food
        food_obj = Food.objects.get(food_id=food_id)
        # check if cart exists 
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_food_in_cart = cart_obj.cartfood_set.filter(food=food_obj)
            # Items already exists in cart
            if this_food_in_cart.exists():
                cartfood = this_food_in_cart.last()
                cartfood.quantity += 1
                cartfood.subtotal += food_obj.food_selling_price
                cartfood.save()
                cart_obj.total += food_obj.food_selling_price
                cart_obj.save()
            # New item is added in cart
            else:
                cartfood = CartFood.objects.create(cart=cart_obj, food=food_obj, price=food_obj.food_selling_price, quantity=1, subtotal=food_obj.food_selling_price)
                cart_obj.total += food_obj.food_selling_price
                cart_obj.save() 
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartfood = CartFood.objects.create(cart=cart_obj, food=food_obj, price=food_obj.food_selling_price, quantity=1, subtotal=food_obj.food_selling_price)
            cart_obj.total += food_obj.food_selling_price
            cart_obj.save()
        return context

class CartView(generic.ListView):
    template_name = 'homepage/cart.html'
    def get(self, request, *args, **kwargs):
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context = {
            'cart': cart,
        }
        return render(request, self.template_name, context)

class ManageView(generic.View):
    def get(self, request, *args, **kwargs):
        cart_food_id = self.kwargs['cartfood_id']
        action = request.GET.get('action')
        # print(cp_id, action)
        cartfood_obj = CartFood.objects.get(id=cart_food_id)
        cart_obj = cartfood_obj.cart
        if action == 'inc':
            cartfood_obj.quantity +=1
            cartfood_obj.subtotal += cartfood_obj.price
            cartfood_obj.save()
            cart_obj.total += cartfood_obj.price
            cart_obj.save()
        elif action == 'dcr':
            cartfood_obj.quantity -= 1
            cartfood_obj.subtotal -= cartfood_obj.price
            cartfood_obj.save()
            cart_obj.total -= cartfood_obj.price
            cart_obj.save()
            if cartfood_obj.quantity == 0:
                cartfood_obj.delete()
        elif action == 'rmv':
            cart_obj.total -= cartfood_obj.subtotal
            cart_obj.save()
            cartfood_obj.delete()
        else:
            print("Something went wrong!!!")
        return redirect('homepage:cart')

class EmptyCartView(generic.View):
    def get(self, request, *args, **kwargs):
        cart_id = request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            cart.cartfood_set.all().delete()
            cart.total = 0
            cart.save()
        return redirect('homepage:cart')

class BlogView(generic.ListView):
    def get(self, request, *args, **kwargs):
        template_name = 'blogs/blog.html'
        blogs_list = Blog.objects.all()
        context = {
            'blogs_list' : blogs_list,
        }
        return render(request, template_name, context)

class BlogDetailView(generic.ListView):
    def get(self, request, *args, **kwargs):
        template_name = 'blogs/blog_detail.html'
        blog_detail_list = Blog.objects.get(blog_id=self.kwargs.get('blog_id'), blog_slug=self.kwargs.get('blog_slug'))
        blog_detail_list.view_count += 1
        blog_detail_list.save()
        comments = BlogReview.objects.filter(blog_id=blog_detail_list.blog_id)
        # print(comments, " comments data")
        context = {
            'blog_detail_list' : blog_detail_list,
            'comments': comments,
        }
        return render(request, template_name, context)

class BlogReviewView(LoginRequiredMixin, generic.CreateView):
    def post(self,request,*args,**kwargs):
        url = request.META.get('HTTP_REFERER')
        try:
            user = request.user.id
            # print(user, " is user")
            blog=self.kwargs.get('blog_id')
            # print(blog, " blog")
            reviews = BlogReview.objects.get(user__id=user, blog_id=blog)
            # print(reviews, " sreviews")
            form = BlogReviewForm(request.POST, instance=reviews)
            # print(form, " Form")
            # print(form.errors)
            form.save()
            return redirect(url)
        except BlogReview.DoesNotExist:
            form = BlogReviewForm(request.POST)
            if form.is_valid():
                blog_data = BlogReview()
                blog_data = form.save(commit=False)
                blog_data.user_id = request.user.id
                # print(blog_data.user_id, " in the user form")
                blog_data.blog_id = blog
                # print(blog_data.blog_id, " in the blog form")
                blog_data.save()
                return redirect(url)

class SearchView(generic.ListView):
    template_name = 'search/search.html'
    def get(self, request, *args, **kwargs):
        search_result = request.GET.get('search')
        if search_result:
            restaurant_result = Restaurant.objects.filter(
                Q(restaurant_name__icontains=search_result) |
                Q(restaurant_address__icontains=search_result) | 
                Q(restaurant_city__icontains=search_result)
                )
            food_result = Food.objects.filter(Q(food_name__icontains=search_result))
        else:
            print("Sorry, no results founds")
        context = {
            'restaurant_result':restaurant_result,
            'food_result' : food_result,
        }
        return render(request, self.template_name, context)

class ContactView(generic.CreateView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            contact_obj = form.save(commit=False)
            contact_obj.save()
            return redirect('homepage:home')
        return render(request, self.template_name, {'form':form})

def vendorMembership(request):
    return render(request, 'vendor/vendor.html')

class CheckoutView(LoginRequiredMixin, generic.CreateView):
    template_name = 'homepage/checkout.html'
    form_class = CheckoutForm
    success_url = reverse_lazy('homepage:payment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
        else:
            cart_obj = None
        context['cart'] = cart_obj
        return context

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            form.instance.cart = cart_obj
            form.instance.subtotal = cart_obj.total
            form.instance.discount = 0 
            form.instance.total = cart_obj.total
            form.instance.order_status = "Order Received"
            del self.request.session['cart_id']
        else:
            return redirect('homepage:checkout')
        return super().form_valid(form)


class MyProfileView(LoginRequiredMixin, generic.ListView):
    template_name = 'profile/userprofile.html'

    def get(self, request):
        # orderid = Order.objects.get(id=id)
        # customer = request.user.customer
        customer = Customer.objects.get(user_id = request.user.id) 
        print(customer, " is logged in")
        orderid = self.kwargs.get('id')
        print(orderid, " ordersssss..... ")
        orders = Order.objects.filter(cart__customer=customer).order_by('-id')
        print(orders, " Orders are")
        context = {
            'orders': orders,
            'customer': customer,
        }
        return render(request, self.template_name, context)

class UserOrderDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'profile/userorderdetail.html'
    def get(self, request, *args, **kwargs):
        # id = self.kwargs.get['pk']
        # user_order = Order.objects.get(id=id).order_by('-id')
        user_order = Order.objects.all().order_by('-id')
        print(user_order, " user orders")
        return render(request, self.template_name, {'user_order':user_order})
    
    # model = Order
    # context_object_name = "order_obj"
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and request.user.customer:
    #         order_id = self.kwargs['pk']
    #         order = Order.objects.get(id=order_id)
    #         if request.user.customer != order.cart.customer:
    #             return redirect('ecomapp:userprofile')
    #     else:
    #         return redirect('/login/?next=/userprofile/')
    #     return super().dispatch(request, *args, **kwargs)
# 


# class MyProfileView(LoginRequiredMixin, generic.ListView):
#     template_name = 'profile/userprofile.html'
#     def get(self, request, *args, **kwargs):
#         # order_id = self.kwargs.get('id')
#         orders = Order.objects.all().order_by('-id')
#         context = {
#             'orders': orders,
#         }
#         return render(request, self.template_name, context)

# class UserOrderDetailView(LoginRequiredMixin, generic.DetailView):
#     template_name = 'profile/userorderdetail.html'
#     def get(self, request, *args, **kwargs):
#         # id = self.kwargs.get['pk']
#         # user_order = Order.objects.get(id=id).order_by('-id')
#         user_order = Order.objects.all().order_by('-id')
#         return render(request, self.template_name, {'user_order':user_order})

def payment(request):
    return render(request, 'homepage/payment.html')

# 
