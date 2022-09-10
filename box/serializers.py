from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Folder,FileStorage

# folder serializers

class FolderSerial(serializers.ModelSerializer):
    
    class Meta:
        model = Folder
        fields = ['id','folder_name','visible','code','date_created',]


class FileSerial(serializers.ModelSerializer):

    class Meta:
        model = FileStorage
        fields = ["id", "idd", "files_name", "files", "image_description", "date_created",]