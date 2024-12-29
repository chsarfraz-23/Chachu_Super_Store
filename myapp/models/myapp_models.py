from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import Permission, AbstractUser, Group
from shortuuid.django_fields import ShortUUIDField


class AuditTrailDateTimeOnly(models.Model):
    id = ShortUUIDField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AuditTrailModel(AuditTrailDateTimeOnly):
    id = ShortUUIDField(primary_key=True)
    created_by = models.ForeignKey(
        "User",
        blank=True,
        null=True,
        related_name="%(class)s_created",
        on_delete=models.CASCADE,
    )
    modified_by = models.ForeignKey(
        "User",
        null=True,
        blank=True,
        related_name="%(class)s_modified",
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class User(AbstractUser, AuditTrailDateTimeOnly):
    phone_number = models.CharField(max_length=20)
    cnic = models.CharField(max_length=244, null=True, blank=True)

    def __str__(self):
        return f"Username={self.username}, password={self.password}"

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class SignUp(AuditTrailDateTimeOnly):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"SignUp(name={self.name}, phone_number={self.phone_number})"

    class Meta:
        verbose_name = "SignUp"
        verbose_name_plural = "SignsUps"


class HomePageProducts(AuditTrailModel):
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


class MainProducts(AuditTrailModel):
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


class Plan(AuditTrailModel):
    id = ShortUUIDField(primary_key=True)
    duration = models.CharField(max_length=200)
    price = models.CharField(max_length=300)
    image = models.ImageField(upload_to="paid_plan")


class Cart(AuditTrailModel):
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


class Challan(AuditTrailModel):
    id = ShortUUIDField(primary_key=True)
    send = models.ImageField(upload_to="challan_requesta")
    email = models.EmailField(max_length=100)


class Temporary(AuditTrailModel):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=300)
    adress = models.CharField(max_length=1000)
    email = models.EmailField(max_length=100, unique=True)
    discount = models.CharField(max_length=400)
    image = models.ImageField(upload_to="home_products")
    postal_code = models.CharField(max_length=100)
    platform = models.CharField(max_length=200)


class Order(AuditTrailModel):
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


class Shop(AuditTrailModel):
    id = ShortUUIDField(primary_key=True)
    shop_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=40)
    cnic = models.CharField(max_length=16)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to="shop_requests")


class ApprovedShops(AuditTrailModel):
    id = ShortUUIDField(primary_key=True)
    shop_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=70)
    password = models.CharField(max_length=40)
    cnic = models.CharField(max_length=16)
    country = models.CharField(max_length=100)
    image = models.ImageField(upload_to="shop_requests")


class ShopsData(AuditTrailModel):
    id = ShortUUIDField(primary_key=True)
    email = models.CharField(max_length=100)
    shop_id = models.CharField(max_length=100, unique=True)
    shop_name = models.CharField(max_length=100)


class ShopProducts(AuditTrailModel):
    id = ShortUUIDField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to="shop_products")


class SendData(AuditTrailModel):
    id = ShortUUIDField(primary_key=True)
    shop_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
