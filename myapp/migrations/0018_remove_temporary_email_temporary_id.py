# Generated by Django 5.0.2 on 2024-05-21 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_remove_challan_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temporary',
            name='email',
        ),
        migrations.AddField(
            model_name='temporary',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
