# Generated by Django 5.0.2 on 2024-05-17 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_home_page_products_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_page_products',
            name='platform',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
