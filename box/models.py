from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserStorageVolume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    volume_in_kb = models.BigIntegerField(default=31457280)


class Folder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=30,blank=False,default="my folder")
    visible = models.BooleanField(default=True)
    code = models.CharField(max_length=30,blank=False)
    anyone_upload = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.folder_name

class FileStorage(models.Model):
    idd = models.CharField(max_length=30,blank=False, default="vxc48sx7f")
    folder = models.ForeignKey(Folder, related_name='folders', on_delete=models.CASCADE)
    files_name = models.CharField(max_length=30000, blank=False, default="image.png")
    files = models.ImageField(upload_to='store/%Y/%m/%d', blank=False)
    image_description = models.TextField(max_length=10000, default="image")
    date_created = models.DateTimeField(auto_now_add=True)
    

