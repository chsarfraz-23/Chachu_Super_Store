from django import forms

class Home_products(forms.Form):   
    choice=[("Main_page","Main_page"),
    ("Central_page","Central_page")
    ]
    platform=forms.ChoiceField(choices=choice,widget=forms.Select(attrs={
        "class":"form-control"
    }))
    name=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Name  of your product "
    }))
    price=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Price of product "
    }))
    adress=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Enter your address"
    }))
    email=forms.EmailField(widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress "
    }))
    discount=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Enter the discount "
    }))
    postal_code=forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Enter your postal code "
    }))
    image=forms.ImageField(widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
    }))
    description=forms.CharField(widget=forms.Textarea(attrs={
        "class":"form-control"
    }))
class Plan_form(forms.Form):
    duration=forms.CharField(max_length=200)
    price=forms.CharField(max_length=300)
    image=forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
    }))
class Upload_challan(forms.Form):
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress "
    }))
    send=forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={
        "class":"form-control"
    }))    
class Sign_up_form(forms.Form):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your user name "
    }))
    first_name=forms.CharField(label="",widget=forms.TextInput(attrs={
        "placeholder":"Enter your first name  "
    }))    
    last_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your last name  "
    }))
    phone_number=forms.CharField(label='',max_length=20,widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone number "
    }))
    email=forms.EmailField(label="",widget=forms.EmailInput(attrs={
        "placeholder":"Enter email adress  "
    }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
    }))
class Login_form(forms.Form):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your Username "
    }))    
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your Password "
    }))

class shop_form(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter Shop name  "
    }))    
    father_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter the shop owner "
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone number "
    }))
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder" : "Enter your email adress "
    }))
    password=forms.CharField(label='',widget=forms.PasswordInput(attrs={
        "placeholder":"Enter your password "
    }))
    cnic=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your cnic ",
        "pattern":"[0-9]{5}-[0-9]{7}-[0-9]{1}"
    }))
    choice_field=[
        ("Pakistan","pakistan"),
        ("India","india"),
        ("Bangladash","Bangladash"),
        ("Afghanistan","Afghanistan"),
        ("Sri-Lanka","Sri-Lanka"),
        ("Nepal","Nepal"),
        ("Iran","Iran"),
        ("Turkey","Turkey")
    ]
    shop_id=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your shop id "
    }))
    country=forms.ChoiceField(choices=choice_field,widget=forms.Select(attrs={
        "class":"form-control"
    }))
    image=forms.ImageField(label='',widget=forms.ClearableFileInput(attrs={
        "class":"form-control "
    }))

class verify_shop(forms.Form):
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress "
    }))
    shop_id=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your Shop ID"
    }))    
    shop_name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your shop name "
    }))
class forget_id_f(forms.Form):
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress "
    }))
class Order_form(forms.Form):
    name=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your name "
    }))
    phone_number=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your phone_number "
    }))
    email=forms.EmailField(label='',widget=forms.EmailInput(attrs={
        "placeholder":"Enter your email adress "
    }))
    adress=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your Adress "
    }))
    postal_code=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your postal code  "
    }))

class My_form(forms.Form):
    username=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder":"Enter your username "
    }))
    password=forms.CharField(label='',widget=forms.TextInput(attrs={
        "placeholder" : "Enter your password "
        }))