# Generated by Django 5.0.2 on 2024-05-26 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0029_shop_products_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop_products",
            name="description",
            field=models.CharField(max_length=1000),
        ),
    ]
