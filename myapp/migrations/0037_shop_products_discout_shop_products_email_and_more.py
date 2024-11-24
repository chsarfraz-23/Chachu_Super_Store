# Generated by Django 5.0.2 on 2024-05-30 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0036_cart_email_main_products_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="shop_products",
            name="discout",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="shop_products",
            name="email",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="shop_products",
            name="platform",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
