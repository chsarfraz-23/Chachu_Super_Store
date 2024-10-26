from rest_framework import serializers
from myapp.models import (
    Main_products,
    Plan,Shop,
    Sign_up,Approved_shops
)
class Main_products_serializer(serializers.ModelSerializer):
    class Meta:
        model=Main_products
        fields=[
            'name','description','price','adress','discount','image','postal_code','platform'
        ]
class Plain_serializer(serializers.ModelSerializer):
    class Meta:
        model=Plan
        fields=[
        'duration','price','image'
        ]
        
class Shop_serializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields=[
            'name','father_name','phone_number','email','password','cnic','country','image'
            ]        
class Signup_serializer(serializers.ModelSerializer):
    class Meta:
        model=Sign_up     
        fields=[
            'name','father_name','phone_number','email','password'
        ]   
class Approvedshops_serializer(serializers.ModelSerializer):
    class Meta:
        model=Approved_shops
        fields=[
            'shop_id','name','father_name','phone_number','email','password','cnic','country','image'
        ]