from rest_framework import serializers
from myapp.models.myapp_models import (
    ApprovedShops,
    MainProducts,
    Plan,
    Shop,
    SignUp,
    User,
)


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "username", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(email=validated_data["email"], username=validated_data["username"])
        user.set_password(validated_data["password"])
        user.save()
        return user


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
        fields = "__all__"


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = "__all__"


class ApprovedShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovedShops
        fields = "__all__"
