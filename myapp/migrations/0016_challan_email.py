# Generated by Django 5.0.2 on 2024-05-21 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_remove_temporary_id_alter_temporary_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="challan",
            name="email",
            field=models.EmailField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
