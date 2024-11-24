from rest_framework import serializers
from myapp.models import (
    ApprovedShops, MainProducts, Plan, Shop, SignUp
)


class MainProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainProducts
        fields = "__all__"


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields="__all__"


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = "__all__"


class ApprovedShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedShops
        fields = "__all__"
