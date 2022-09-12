from django.contrib import admin
from .models import Folder, FileStorage, UserStorageVolume

# Register your models here.

admin.site.register(Folder)
admin.site.register(FileStorage)
admin.site.register(UserStorageVolume)
