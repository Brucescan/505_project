# Generated by Django 4.2 on 2024-12-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="phone",
            field=models.CharField(max_length=50, verbose_name="联系电话"),
        ),
    ]
