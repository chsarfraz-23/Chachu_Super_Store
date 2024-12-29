from django.shortcuts import render, redirect, reverse
from myapp.form import (
    HomeProducts,
    UploadChallan,
    ShopForm,
    VerifyShop,
    ForgetIdForm,
    OrderForm,
    MyForm,
    SignUpForm,
    LoginForm,
)
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
    SignUp,
    HomePageProducts,
    MainProducts,
)
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework import status

from rest_framework.response import Response
from myapp.serializers import (
    MainProductSerializer,
    PlanSerializer,
    ShopSerializer,
    SignupSerializer,
    ApprovedShopSerializer,
)
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
import sqlite3

from myapp.tasks import shop_approval_msg

connection = sqlite3.connect("db.sqlite3", check_same_thread=False)
cursor = connection.cursor()


def my_verification(a):
    def my_function(request, *args, **Kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return a(request, *args, **Kwargs)
        else:
            my_url = reverse("home")
            return HttpResponseRedirect(my_url)

    return my_function


@api_view(["GET", "POST", "DELETE"])
def Home(request):
    sarfraz = SignUp.objects.all()
    if request.method == "DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == "POST":
        my_serializer = SignupSerializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        my_serializer = SignupSerializer(sarfraz, many=True)
        return Response(my_serializer.data, status=status.HTTP_200_OK)


@api_view(["POST", "GET", "DELETE"])
def post(request):
    sarfraz = HomePageProducts.objects.all()
    if request.method == "POST":
        my_serializer = MainProductSerializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == "GET":
        my_serializer = MainProductSerializer(sarfraz, many=True)
        return Response(my_serializer.data)
    elif request.method == "DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["PUT", "PATCH", "DELETE", "GET"])
def mannually(request, id):
    sarfraz = HomePageProducts.objects.get(pk=id)
    if request.method == "PUT":
        my_serializer = MainProductSerializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        sarfraz.name = request.data.get("name", sarfraz.name)
        sarfraz.description = request.data.get("description", sarfraz.description)
        sarfraz.price = request.data.get("price", sarfraz.price)
        sarfraz.adress = request.data.get("adress", sarfraz.adress)
        sarfraz.discount = request.data.get("discount", sarfraz.discount)
        sarfraz.image = request.data.get("iamge", sarfraz.image)
        sarfraz.postal_code = request.data.get("postal_code", sarfraz.postal_code)
        sarfraz.platform = request.data.get("platform", sarfraz.platform)
        sarfraz.save()
        my_serializer = MainProductSerializer(sarfraz)
        return Response(my_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == "GET":
        my_serializer = MainProductSerializer(sarfraz)
        return Response(my_serializer.data, status=status.HTTP_200_OK)


@api_view(["GET", "POST", "DELETE"])
def paid_plan(request):
    sarfraz = Plan.objects.all()
    if request.method == "POST":
        my_serializer = PlanSerializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "GET":
        my_serializer = PlanSerializer(sarfraz, many=True)
        return Response(my_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["GET", "DELETE"])
def main_products_api(request):
    sarfraz = MainProducts.objects.all()
    if request.method == "GET":
        my_serializer = MainProductSerializer(sarfraz, many=True)
        return Response(my_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["POST", "GET", "DELETE", "PATCH"])
def shop_api(request, id):
    sarfraz = Shop.objects.get(pk=id)
    if request.method == "POST":
        my_serializer = ShopSerializer(data=request.data)
        if my_serializer.is_valid():
            my_serializer.save()
            return Response(my_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "GET":
        my_serializer = ShopSerializer(sarfraz)
        return Response(my_serializer.data, status=status.HTTP_200_OK)
    elif request.method == "DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == "PATCH":
        sarfraz.name = request.data.get("name", sarfraz.name)
        sarfraz.father_name = request.data.get("father_name", sarfraz.father_name)
        sarfraz.phone_number = request.data.get("phone_number", sarfraz.phone_number)
        sarfraz.email = request.data.get("email", sarfraz.email)
        sarfraz.password = request.data.get("password", sarfraz.password)
        sarfraz.cnic = request.data.get("cnic", sarfraz.cnic)
        sarfraz.country = request.data.get("country", sarfraz.country)
        sarfraz.image = request.data.get("image", sarfraz.image)
        sarfraz.save()
        return Response(status=status.HTTP_200_OK)


@api_view(["DELETE"])
def shop_overall(request):
    sarfraz = Shop.objects.all()
    if request.method == "DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["POST", "GET", "DELETE"])
def approve_shop_api(request):
    approved_shops = ApprovedShops.objects.all()
    if request.method == "POST":
        my_serializer = ApprovedShopSerializer(data=request.data)
        if my_serializer.is_valid():
            shop_approved = my_serializer.save()
            shop_approval_msg.delay(approved_shop=shop_approved)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        my_serializer = ApprovedShopSerializer(approved_shops, many=True)
        return Response(my_serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        obj = ShopsData.objects.all()
        obj.delete()
        obj1 = ShopProducts.objects.all()
        obj1.delete()
        obj2 = SendData.objects.all()
        obj2.delete()
        obj4 = Temporary.objects.all()
        obj4.delete()
        obj3 = Shop.objects.all()
        obj3.delete()
        approved_shops.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(["DELETE"])
def shop_data(request):
    sarfraz = ShopsData.objects.all()
    if request.method == "DELETE":
        sarfraz.delete()
        return Response(status=status.HTTP_200_OK)


@login_required(login_url="home")
def home_page(request):
    obj1 = HomePageProducts.objects.all()
    obj2 = MainProducts.objects.all()
    context = {"object1": obj1, "object2": obj2}
    return render(request, "homepage.html", context)


@login_required(login_url="home")
def upload_products(request):
    form = HomeProducts()
    if request.method == "POST":
        form = HomeProducts(request.POST, request.FILES)
        if form.is_valid():
            platform = request.POST["platform"]
            if platform == "Main_page":
                try:
                    Temporary.objects.create(**form.cleaned_data)
                    return redirect("paid_plan/")
                except Exception:
                    messages.success(
                        request, "Sorry !!! Only one plan is allowed at one time "
                    )

            else:
                HomePageProducts.objects.create(**form.cleaned_data)
                messages.success(request, "Product uploaded to Home page  !!! ")
    context = {"form": form}
    return render(request, "sale.html", context)


def paid_services(request):
    obj = Plan.objects.all()
    context = {"object": obj}
    return render(request, "paid_services.html", context)


def cart(request, id):
    obj = HomeProducts.objects.get(pk=id)
    try:
        Cart.objects.create(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            price=obj.price,
            adress=obj.adress,
            email=obj.email,
            discount=obj.discount,
            image=obj.image,
            postal_code=obj.postal_code,
            platform=obj.platform,
        )
        my_url = reverse("main_page")
        return HttpResponseRedirect(my_url)
    except Exception:
        messages.success(request, "The product is alredy in the cart !!")
        my_url = reverse("main_page")
        return HttpResponseRedirect(my_url)


def cart_main(request, id, id2):
    obj = MainProducts.objects.get(pk=id2)
    try:
        Cart.objects.create(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            price=obj.price,
            adress=obj.adress,
            email=obj.email,
            discount=obj.discount,
            image=obj.image,
            postal_code=obj.postal_code,
            platform=obj.platform,
        )
        my_url = reverse("main-detail", args=[id])
        messages.success(request, "The product added to the cart ")
        return HttpResponseRedirect(my_url)
    except Exception:
        my_url = reverse("main-detail", args=[id])
        print("sarfraz saleem ")
        messages.success(request, "The product is already in the cart ")
        return HttpResponseRedirect(my_url)


def shop_cart(request, id, id2):
    obj = ShopProducts.objects.get(pk=id2)
    try:
        Cart.objects.create(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            price=obj.price,
            adress=obj.adress,
            email=obj.email,
            discount=obj.discount,
            image=obj.image,
            postal_code=obj.postal_code,
            platform=obj.platform,
        )
        return HttpResponse(
            "<h1 align='center'>Product added to the card successfully !! </h1>"
        )
    except Exception:
        return HttpResponse(
            "<h1 align='center'>The product is already added to the cart !!! </h1>"
        )


def check_cart(request):
    obj = Cart.objects.all()
    context = {"object": obj}
    return render(request, "cart.html", context)


def check_plan(request):
    obj = Plan.objects.all()
    context = {"object": obj}
    return render(request, "check_plan.html", context)


def admin_verification(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            name = request.POST["username"]
            password = request.POST["password"]
            query = (
                f"select* from myapp_admin_verification where pasword= '{password}' "
            )
            cursor.execute(query)
            variable = cursor.fethone()
            if variable is not None:
                if name == variable[1]:
                    return redirect("admin_login/")
                else:
                    messages.success(request, "The user name is not valid  !! ")
    context = {"form": form}
    return render(request, "admin_verification.html", context)


def admin_plans(request):
    return render(request, "admin_plan.html")


def empty(my_list, new_list=[], nn=0):
    for i in my_list:
        new_list.append(1)
    del my_list[nn : sum(new_list)]
    return my_list


def remove_from_cart(request, id):
    try:
        obj = Cart.objects.get(pk=id)
        obj.delete()
        my_url = reverse("check-cart")
        messages.success(request, "The product is removed successfully !! ")
        return HttpResponseRedirect(my_url)
    except Exception:
        messages.success(
            request, "You have already removed the product from the cart !! "
        )
        my_url = reverse("check-cart")
        return HttpResponseRedirect(my_url)


def choose_plan(request):
    return render(request, "choose_plan.html")


def upload_challan(request):
    form = UploadChallan()
    if request.method == "POST":
        form = UploadChallan(request.POST, request.FILES)
        if form.is_valid():
            name = request.POST["email"]
            check_list = []
            query = "select* from myapp_sign_up"
            cursor.execute(query)
            variable = cursor.fetchall()
            for i in variable:
                check_list.append(i[4])
            if name in check_list:
                Challan.objects.create(**form.cleaned_data)
                messages.success(request, "Challan Uploaded Successfully !!! ")
            else:
                messages.success(
                    request, "Sorry !! This email adress is not registered "
                )
    context = {"form": form}
    return render(request, "upload_challan.html", context)


@my_verification
def view_challan(request):
    obj = Challan.objects.all()
    context = {"object": obj}
    return render(request, "view_requests.html", context)


def reject_challan(request, id):
    try:
        obj = Challan.objects.get(pk=id)
        obj.delete()
        return HttpResponse(
            "<h1 align='center'>Challan is rejected sucsessfully !!</h1>"
        )
    except Exception:
        return HttpResponse(
            "<h1 align='center'>The challan is already rejected !! </h1>"
        )


def front_page(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username1 = request.POST["username"]
            first_name1 = request.POST["first_name"]
            last_name1 = request.POST["last_name"]
            email1 = request.POST["email"]
            password1 = request.POST["password"]
            phone_number1 = request.POST["phone_number"]
            try:
                User.objects.create(
                    username=username1,
                    first_name=first_name1,
                    last_name=last_name1,
                    email=email1,
                    password=password1,
                    is_staff=False,
                )
                UserProfile.objects.create(phone_number=phone_number1)
                messages.success(request, "Account created Successfully !!! ")
                my_reverse = reverse("main")
                return HttpResponseRedirect(my_reverse)
            except Exception:
                messages.success(
                    request,
                    "The user name already taken !! Please try with another  ",
                )
    context = {"form": form}
    return render(request, "front_page.html", context)


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            name1 = request.POST["username"]
            password1 = request.POST["password"]
            user = authenticate(username=name1, password=password1)
            print(user)
            if user is not None:
                login(request, user)
                return redirect("main/")
            else:
                messages.success(
                    request, "There is some problem in your data.Please try  again !!! "
                )
    context = {"form": form}
    return render(request, "login.html", context)


def logout_main(request):
    logout(request)
    my_reverse = reverse("home")
    return HttpResponseRedirect(my_reverse)


def allow_main(request, *args, **kwargs):
    query = "select* from myapp_temporary"
    cursor.execute(query)
    variable = cursor.fetchone()
    MainProducts.objects.create(
        name=variable[0],
        description=variable[1],
        price=variable[2],
        adress=variable[3],
        discount=variable[4],
        image=variable[5],
        postal_code=variable[6],
        platform=variable[7],
    )
    return HttpResponse(
        "<h1 align='center'>The product is uploaded to the main page !!!</h1>"
    )


def order_now(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            email_list = []
            query = "select* from myapp_cart "
            cursor.execute(query)
            variable = cursor.fetchall()
            for i in variable:
                email_list.append(i[9])
            name = request.POST["name"]
            phone_number = request.POST["phone_number"]
            email = request.POST["email"]
            postal_code = request.POST["postal_code"]
            new_context = {
                "name": name,
                "phone_number": phone_number,
                "email": email,
                "postal_code": postal_code,
            }
            my_subject = "Products Order email "
            html_message = render_to_string("orders_email.html", new_context)
            plain_message = strip_tags(html_message)
            message = EmailMultiAlternatives(
                body=plain_message, subject=my_subject, from_email=None, to=email_list
            )
            message.attach_alternative(html_message, "text/html")
            # message.send()
            messages.success(request, "You have ordered your products successfully !! ")
    cotext = {"form": form}
    return render(request, "order_now.html", cotext)


def open_your_shop(request):
    form = ShopForm()
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            email = request.POST["email"]
            check_list = []
            query = "select* from myapp_approved_shops"
            cursor.execute(query)
            variable = cursor.fetchall()
            shop_id = request.POST["shop_id"]
            check_list1 = []
            query1 = "select* from myapp_shops_data "
            cursor.execute(query1)
            variable1 = cursor.fetchall()
            query2 = "select* from myapp_send_data "
            check_list2 = []
            cursor.execute(query2)
            variable2 = cursor.fetchall()
            for i in variable2:
                check_list2.append(i[1])
            print(email)
            print(check_list2)
            if email in check_list2:
                messages.success(
                    request, "Only one shop is allowed at one email adress !!"
                )
            else:
                for i in variable1:
                    check_list1.append(i[2])
                for i in variable:
                    check_list.append(i[8])
                if shop_id in check_list or shop_id in check_list1:
                    messages.success(
                        request, "The shop with this id is already approved !! "
                    )
                else:
                    try:
                        Shop.objects.create(**form.cleaned_data)
                        messages.success(
                            request,
                            "Your detail is send successfully !! We will verify your shop as soon as possible ",
                        )
                    except Exception:
                        messages.success(
                            request, "The Shop with this ID is already registerd !!"
                        )
    context = {"form": form}
    return render(request, "shop.html", context)


def show_shop_data(request):
    object = Shop.objects.all()
    context = {"object": object}
    return render(request, "show_shop.html", context)


def approve_shop(request, id):
    obj = Shop.objects.get(pk=id)
    ApprovedShops.objects.create(
        name=obj.name,
        father_name=obj.father_name,
        phone_number=obj.phone_number,
        email=obj.email,
        password=obj.password,
        cnic=obj.cnic,
        shop_id=obj.shop_id,
        country=obj.country,
        image=obj.image,
    )
    ShopsData.objects.create(shop_id=obj.shop_id, shop_name=obj.name, email=obj.email)
    SendData.objects.create(
        name=obj.name,
        shop_id=obj.shop_id,
        email=obj.email,
    )
    obj.delete()
    return HttpResponse(
        "<h1 align='center'>The shop is approved successfully !!! </h1>"
    )


def shopping_stores(request):
    obj = ApprovedShops.objects.all()
    context = {"object": obj}
    return render(request, "shops_page.html", context)


def reject_shop_request(request, id):
    obj = Shop.objects.get(pk=id)
    obj.delete()
    return HttpResponse(
        "<h1 align='center'>The Request has been rejected successfully !! </h1>"
    )


def verify_shop_f(request):
    form = VerifyShop()
    if request.method == "POST":
        form = VerifyShop(request.POST)
        if form.is_valid():
            shop_id = request.POST["shop_id"]
            email = request.POST["email"]
            shop_name = request.POST["shop_name"]
            query = f"select* from myapp_shops_data where shop_id = '{shop_id}' "
            cursor.execute(query)
            variable = cursor.fetchone()
            if variable is not None:
                if variable[0] == shop_name and variable[1] == email:
                    return redirect(f"shop/{shop_id}/")
                else:
                    messages.success(request, "Invalid Credentials !!!!")
            else:
                return HttpResponse(
                    "<h1 align='center'>No Shop  with this data is registered !! </h1>"
                )
    context = {"form": form}
    return render(request, "verify_shop.html.", context)


def my_shop(request, id):
    obj1 = ApprovedShops.objects.get(pk=id)
    context = {
        "object1": obj1,
    }
    return render(request, "main_shop.html", context)


def forget_id(request):
    form = ForgetIdForm()
    if request.method == "POST":
        form = ForgetIdForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            query = f"select* from myapp_send_data where email = '{email}'"
            cursor.execute(query)
            variable = cursor.fetchone()
            if variable is not None:
                new_context = {"shop_id": variable[0], "shop_name": variable[2]}
                my_subject = "Shop Data  recovery Email "
                html_message = render_to_string("forget_email.html", new_context)
                plain_message = strip_tags(html_message)
                message = EmailMultiAlternatives(
                    body=plain_message, subject=my_subject, from_email=None, to=[email]
                )
                message.attach_alternative(html_message, "text/html")
                try:
                    message.send()
                    messages.success(
                        request, "The email is sent your verified email adress !! "
                    )
                except Exception:
                    messages.success(
                        request, "There is some problem please try again !!! "
                    )
            else:
                messages.success(request, "The email is not verified !!! ")
    context = {"form": form}
    return render(request, "forget_id.html", context)


def main_products_detail(request, id):
    obj = MainProducts.objects.get(pk=id)
    context = {"object": obj}
    return render(request, "main_products_detail.html", context)


@login_required(login_url="verify_shop/")
def upload_product_on_shop(request, id):
    form = HomeProducts()
    if request.method == "POST":
        form = HomeProducts(request.POST, request.FILES)
        if form.is_valid():
            ShopProducts.objects.create(**form.cleaned_data)
            messages.success(request, "The product is uploaded successfully !! ")
    context = {"form": form}
    return render(request, "shop_products_upload.html", context)


def shops_data_home(request, id):
    obj = ApprovedShops.objects.get(pk=id)
    obj2 = ShopProducts.objects.all()
    context = {"object": obj, "object2": obj2}
    return render(request, "shop_products_data_home.html", context)


# def admin_verification(request):
#     form=admin_verification_form()
#     if request.method=="POST":
#         form=admin_verification(request.POST)
#         if form.is_valid():
#             pass

#     context={
#         "form":form
#     }
#     return render(request,"admin_verification_form.html",context)
