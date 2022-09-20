from django.db import models
from account.models import User
from gdstorage.storage import GoogleDriveStorage

# Create your models here.

gd_storage = GoogleDriveStorage()

class UserStorageVolume(models.Model):
    user = models.fieldName = models.OneToOneField(User, on_delete=models.CASCADE)
    volume_in_kb = models.BigIntegerField(default=31457280)

    def __str__(self):
        return "{0} ------ {1}".format(self.volume_in_kb, self.user.email)


class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=30, blank=False, default="my folder")
    visible = models.BooleanField(default=True)
    code = models.CharField(max_length=30, blank=False)
    anyone_upload = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folder_name


class FileStorage(models.Model):
    idd = models.CharField(max_length=30, blank=False, default="vxc48sx7f")
    folder = models.ForeignKey(Folder, related_name="folders", on_delete=models.CASCADE)
    files_name = models.CharField(max_length=30000, blank=False, default="image.png")
    files = models.ImageField(upload_to="store/%Y/%m/%d", blank=False, storage=gd_storage)
    image_description = models.TextField(max_length=10000, default="image")
    date_created = models.DateTimeField(auto_now_add=True)
