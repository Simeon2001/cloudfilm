from .models import Folder,FileStorage, UserStorageVolume
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
    parser_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .serializers import FileSerial
from rest_framework.parsers import FileUploadParser,FormParser,MultiPartParser
from PIL import Image
import os
from .idd_hash import id_hash

# Create your views here.

@api_view(["GET",'POST',"DELETE"])
@permission_classes([IsAuthenticated])
@parser_classes([FileUploadParser])
def upload_file(request,code):
    current_user = request.user
    folder = Folder.objects.get(code=code)
    update_volume = UserStorageVolume.objects.get(user=folder.user)
    cloud_volume,created = UserStorageVolume.objects.get_or_create(user=folder.user)
    print(cloud_volume.volume_in_kb)
    if request.method == "POST":
        try:
            image = request.data["file"]
            if folder.anyone_upload == False and current_user == folder.user or folder.anyone_upload == True:
                    img = Image.open(image)
                    byte_size = int(len(img.fp.read()))
                    if byte_size > int(cloud_volume.volume_in_kb):
                        return Response(status=404) 
                    else:
                        new_volume = int(cloud_volume.volume_in_kb) - byte_size
                        idd = id_hash(image.name, folder.id)
                        print(byte_size)
                        print(new_volume)
                        descrpt = "just a image"
                        print(img.verify())
                        print(image.name)

                        save_image = FileStorage.objects.create(idd=idd, folder = folder, files_name=image.name, 
                                                                files=image, image_description=descrpt)
                        update_volume.volume_in_kb = new_volume
                        update_volume.save()
                        return Response(status=201)

            return Response(status=204)
        except:
            Response(status=404)
    
    if request.method == "DELETE":
        id = request.data.get("id")


    else:
        if folder.visible == True or current_user == folder.user:
            get_img = FileStorage.objects.filter(folder=folder)
            serializer_class = FileSerial(get_img,many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        else:
            return Response(status=404)
