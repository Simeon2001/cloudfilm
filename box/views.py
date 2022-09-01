from django.shortcuts import render, HttpResponse
from .models import Folder,FileStorage, UserStorageVolume
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
    parser_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .serializers import FolderSerial, FileSerial
from .hash import hashes
from rest_framework.parsers import FileUploadParser,FormParser,MultiPartParser
from PIL import Image
import os

# Create your views here.

@api_view(["GET",'POST'])
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def index(request):
    user = request.user
    if request.method == "POST":
        folder_name = request.data.get("name")
        code = hashes()
        visible = request.data.get("visible")
        anyone_upload = request.data.get("anyone_upload")
        data = Folder.objects.create(user=user, folder_name=folder_name, visible=visible,
                                    code=code, anyone_upload=anyone_upload)
        serializer_class = FolderSerial(data)
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)
    else:
        folder = Folder.objects.filter(user=user)
        serializer_class = FolderSerial(folder,many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

@api_view(["GET",'POST'])
@permission_classes([IsAuthenticated])
@parser_classes([FileUploadParser])
def upload_file(request,code):
    current_user = request.user
    folder = Folder.objects.get(code=code)
    update_volume = UserStorageVolume.objects.get(user=folder.user)
    cloud_volume,created = UserStorageVolume.objects.get_or_create(user=folder.user)
    print(cloud_volume.volume_in_kb)
    if request.method == "POST":
        image = request.data["file"]
        if folder.anyone_upload == False and current_user == folder.user or folder.anyone_upload == True:
            try:
                img = Image.open(image)
                byte_size = int(len(img.fp.read()))
                if byte_size > int(cloud_volume.volume_in_kb):
                    return Response(status=404) 
                else:
                    new_volume = int(cloud_volume.volume_in_kb) - byte_size
                    print(byte_size)
                    print(new_volume)
                    descrpt = "just a image"
                    print(img.verify())
                    print(image.name)

                    save_image = FileStorage.objects.create(folder = folder, files_name=image.name, 
                                                            files=image, image_description=descrpt)
                    update_volume.volume_in_kb = new_volume
                    update_volume.save()
                    return Response(status=201)

            except:
                return Response(status=404)
        return Response(status=204)

    else:
        get_img = FileStorage.objects.filter(folder=folder)
        serializer_class = FileSerial(get_img,many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)
        