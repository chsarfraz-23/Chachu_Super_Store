# Generated by Django 5.0.2 on 2024-05-26 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0025_approved_shops"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="approved_shops",
            name="id",
        ),
        migrations.RemoveField(
            model_name="shop",
            name="id",
        ),
        migrations.AddField(
            model_name="approved_shops",
            name="shop_id",
            field=models.CharField(
                default="", max_length=100, primary_key=True, serialize=False
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="shop",
            name="shop_id",
            field=models.CharField(
                default=1, max_length=100, primary_key=True, serialize=False
            ),
            preserve_default=False,
        ),
    ]
