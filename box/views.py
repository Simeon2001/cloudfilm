from box.models import Folder, FileStorage, UserStorageVolume
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
    parser_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from box.serializers import FileSerial
from rest_framework.parsers import FileUploadParser
from PIL import Image
from box.idd_hash import id_hash
from folderapp import resp
from box.uploader import read_image


# File uploading,displaying images function
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
@parser_classes([FileUploadParser])
def upload_file(request, code):
    current_user = request.user
    try:
        folder = Folder.objects.get(code=code)
        update_volume = UserStorageVolume.objects.get(user=folder.user)

        print(update_volume.volume_in_kb)

        # Post request: to add new image to album
        if request.method == "POST":
            try:
                image = request.data["file"]
                if (
                    folder.anyone_upload == False
                    and current_user == folder.user
                    or folder.anyone_upload == True
                ):

                    img = Image.open(image)
                    byte_size = int(len(img.fp.read()))
                    if byte_size > int(update_volume.volume_in_kb):
                        return resp.forbidden("insufficient cloud space")
                    else:
                        new_volume = int(update_volume.volume_in_kb) - byte_size
                        idd = id_hash(image.name, folder.id)
                        print(byte_size)
                        print(new_volume)

                        status, descrpt = read_image(img)
                        if status != 200:
                            return resp.down("something wrong")
                        else:
                            print(img.verify())
                            print(image.name)

                            save_image = FileStorage.objects.create(
                                idd=idd,
                                folder=folder,
                                files_name=image.name,
                                files=image,
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

        # Get request: to get all images
        else:
            if folder.visible == True or current_user == folder.user:
                get_img = FileStorage.objects.filter(folder=folder)
                serializer_class = FileSerial(get_img, many=True)
                return Response(serializer_class.data, status=status.HTTP_200_OK)

            else:
                return resp.not_yours("not your account")
    except:
        return resp.not_found("image album not found")


# Delete request function to delete image
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_file(request, code, idd):
    current_user = request.user
    try:
        folder = Folder.objects.get(code=code)

        # Delete Request: to delete an image
        if current_user == folder.user:
            del_img = FileStorage.objects.get(folder=folder, idd=idd)
            del_img.delete()
            return resp.it_ok("image deleted")
        else:
            return resp.not_yours("not your account")
    except:
        return resp.not_found("image or album not found")


# request function to check your remaining storage space
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def storage_metrics(request):
    current_user = request.user
    get_volume = UserStorageVolume.objects.get(user=current_user)
    space_in_mb = int(get_volume.volume_in_kb) / (1024 * 1024)
    return Response(
        {"status":True,
        "space_in_kb": get_volume.volume_in_kb,
        "space_in_mb": space_in_mb,
        }
    )
        
    

