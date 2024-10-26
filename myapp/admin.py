from django.contrib import admin
from myapp.models import (
    Home_page_products,
    Main_products,
    Plan,Cart,Challan,Sign_up,Temporary,Shop,Approved_shops,Shops_data,Shop_products,Send_data,UserProfile
)
# Register your models here.
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User
class UserProfileInline(admin.StackedInline):
    model=UserProfile
    can_delete=False
class AccountsUserAdmin(AuthUserAdmin):
    def add_view(*args,**kwargs):
        self.inlines=[]
        return super(AccountsUserAdmin,self).add_view(*args,**kwargs)
    def change_view(*args,**kwargs):
        self.inlines=[AccountsUserAdmin]
        return super(AccountsUserAdmin,self).change_view(*args,**kwargs)  
admin.site.unregister(User)
admin.site.register(User,AccountsUserAdmin)        
admin.site.register(Home_page_products)
admin.site.register(Main_products)
admin.site.register(Plan)
admin.site.register(Cart)
admin.site.register(Challan)
admin.site.register(Sign_up)
admin.site.register(Temporary)
admin.site.register(Shop)
admin.site.register(Approved_shops)
admin.site.register(Shops_data)
admin.site.register(Shop_products)
admin.site.register(Send_data)