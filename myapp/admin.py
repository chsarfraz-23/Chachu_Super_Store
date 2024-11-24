from django.contrib import admin
from myapp.models import (
    Plan,
    Cart,
    Challan,
    Temporary,
    Shop,
    ApprovedShops,
    ShopsData,
    ShopProducts,
    SendData,
    UserProfile,
    HomePageProducts,
    MainProducts,
    SignUp,
)

# Register your models here.
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class AccountsUserAdmin(AuthUserAdmin):
    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(AccountsUserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [AccountsUserAdmin]
        return super(AccountsUserAdmin, self).change_view(*args, **kwargs)


admin.site.unregister(User)
admin.site.register(User, AccountsUserAdmin)
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
