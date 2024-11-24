from django.db import models
from django.dispatch import receiver
from django .db.models.signals import (
    post_save
)
from django.dispatch import receiver
from  django.db.models.signals import(
    pre_save,
    post_save
)
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from shortuuid.django_fields import ShortUUIDField

class UserProfile(models.Model):
    id = ShortUUIDField(primary_key=True)
    user = models.OneToOneField(User, on_delete = models.CASCADE,null=True)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.username


@receiver(post_save, sender=User)
def user_action(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("The additional field for the user has been created !!! ")
    else:
        print("The user crestion is failed ")    


class SignUp(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=200,primary_key=True)
    password = models.CharField(max_length=100)


class HomePageProducts(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=300)
    adress = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)
    discount = models.CharField(max_length=400)
    image = models.ImageField(upload_to="home_products")
    postal_code = models.CharField(max_length=100)
    platform = models.CharField(max_length=200)


class MainProducts(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    adress = models.CharField(max_length=400)
    image = models.ImageField(upload_to="main_products")
    discount = models.CharField(max_length=400)
    postal_code = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)


class Plan(models.Model):
    id = ShortUUIDField(primary_key=True)
    duration = models.CharField(max_length=200)
    price = models.CharField(max_length=300)
    image = models.ImageField(upload_to="paid_plan")


class Cart(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=300)
    adress = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)
    discount = models.CharField(max_length=400)
    image = models.ImageField(upload_to="home_products")
    postal_code = models.CharField(max_length=100)
    platform = models.CharField(max_length=200)

class Challan(models.Model):
    id = ShortUUIDField(primary_key=True)
    send = models.ImageField(upload_to="challan_requesta")
    email = models.EmailField(max_length=100)


class Temporary(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=300)
    adress = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100,primary_key=True)
    discount = models.CharField(max_length=400)
    image = models.ImageField(upload_to="home_products")
    postal_code = models.CharField(max_length=100)
    platform = models.CharField(max_length=200)


class Order(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=300)
    adress = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100)
    discount = models.CharField(max_length=400)
    image = models.ImageField(upload_to="home_products")
    postal_code = models.CharField(max_length=100)
    platform = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Shop(models.Model):
    id = ShortUUIDField(primary_key=True)
    shop_id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=40)
    cnic = models.CharField(max_length=16)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shop_requests')


class ApprovedShops(models.Model):
    id = ShortUUIDField(primary_key=True)
    shop_id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=40)
    cnic = models.CharField(max_length=16)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shop_requests')


class ShopsData(models.Model):
    id = ShortUUIDField(primary_key=True)
    email = models.CharField(max_length=100)
    shop_id = models.CharField(max_length=100,primary_key=True)
    shop_name = models.CharField(max_length=100)


class ShopProducts(models.Model):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shop_products')


class SendData(models.Model):
    id = ShortUUIDField(primary_key=True)
    shop_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,primary_key=True)
    






