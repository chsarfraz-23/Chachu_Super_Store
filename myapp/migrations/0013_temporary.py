# Generated by Django 5.0.2 on 2024-05-21 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0012_remove_sign_up_id_alter_sign_up_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Temporary",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("description", models.CharField(max_length=1000)),
                ("price", models.CharField(max_length=300)),
                ("adress", models.CharField(max_length=1000)),
                ("discount", models.CharField(max_length=400)),
                ("image", models.ImageField(upload_to="home_products")),
                ("postal_code", models.CharField(max_length=100)),
                ("platform", models.CharField(max_length=200)),
            ],
        ),
    ]
