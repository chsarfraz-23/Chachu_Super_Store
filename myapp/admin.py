from django.contrib import admin
from django.contrib.admin import register

from myapp.models.myapp_models import (
    Plan,
    Cart,
    Challan,
    Temporary,
    Shop,
    ApprovedShops,
    ShopsData,
    ShopProducts,
    SendData,
    HomePageProducts,
    MainProducts,
    SignUp,
    User,
)


@register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "phone_number", "email")
    readonly_fields = ("id", "password")


admin.site.register(HomePageProducts)
admin.site.register(MainProducts)
admin.site.register(Plan)
admin.site.register(Cart)
admin.site.register(Challan)
admin.site.register(SignUp)
admin.site.register(Temporary)
admin.site.register(Shop)
admin.site.register(ApprovedShops)
admin.site.register(ShopsData)
admin.site.register(ShopProducts)
admin.site.register(SendData)
