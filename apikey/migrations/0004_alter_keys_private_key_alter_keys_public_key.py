# Generated by Django 4.0.1 on 2022-09-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apikey", "0003_alter_keys_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="keys",
            name="private_key",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="keys",
            name="public_key",
            field=models.CharField(max_length=50),
        ),
    ]
