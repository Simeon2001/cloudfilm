import base64
import io

from folderapp import resp
from PIL import Image
from rest_framework import status
from rest_framework.decorators import (api_view, authentication_classes,
                                       parser_classes, permission_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from box.idd_hash import id_hash
from box.models import FileStorage, Folder, UserStorageVolume
from box.uploader import read_image


# request function to save base64 image from internal microservice api
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_basefile(request, code):
    current_user = request.user
    try:
        folder = Folder.objects.get(code=code)
        update_volume = UserStorageVolume.objects.get(user=folder.user)

# Post request: to add new image to album
        if request.method == "POST":
            try:
                image = request.data.get("imgbase")
                img_name = request.data.get("imgname")
                if (
                    folder.anyone_upload == False
                    and current_user == folder.user
                    or folder.anyone_upload == True
                ):
                    
                    de_img = io.BytesIO(base64.b64decode(image))
                    img = Image.open(de_img)
                    byte_size = int(len(img.fp.read()))
                    if byte_size > int(update_volume.volume_in_kb):
                        return resp.forbidden("insufficient cloud space")
                    

                    else:
                        new_volume = int(update_volume.volume_in_kb) - byte_size
                        idd = id_hash(img_name, folder.id)
                        print(byte_size)
                        print(new_volume)

# get image details using ML
                        status, descrpt = read_image(img)
                        if status != 200:
                           return resp.down("something wrong") 
                        else:
                            print(img.verify())
                            print(img_name)

                            save_image = FileStorage.objects.create(
                                idd=idd,
                                folder=folder,
                                files_name=img_name,
                                files=de_img,
                                image_description=descrpt,
                            )
                            update_volume.volume_in_kb = new_volume
                            update_volume.save()
                            return resp.accepted("image saved")

                return resp.not_yours("sorry you can't upload to this album")
            except:
                return resp.media_error(
                    "uploading wrong image, make sure you are uploading jpg, jpeg, png files"
                )

    except:
        return resp.not_found("image album not found")            


# testing function            
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@parser_classes([FileUploadParser])
def upload_file(request, code):
    if request.method == "POST":
        image = request.data["file"]
        img = Image.open(image)
        
        print(img)
        return resp.accepted("image")