# Generated by Django 4.0.1 on 2022-08-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("box", "0004_filestorage_userstoragevolume_folder_anyone_upload_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="filestorage",
            name="files_image",
            field=models.CharField(default="image.png", max_length=30000),
        ),
    ]
