# Generated by Django 3.2.5 on 2022-11-02 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default='Goku Adhikari', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='fullname',
            field=models.CharField(default='Thulobharyang', max_length=50),
            preserve_default=False,
        ),
    ]
