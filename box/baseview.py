from .models import Folder, FileStorage, UserStorageVolume
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
    parser_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from PIL import Image
import io
import base64
from .idd_hash import id_hash
from folderapp import resp

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def upload_basefile(request, code):
    

        # Post request: to add new image to album
        if request.method == "POST":
            
                image = request.data.get("imgbase")
                img_name = request.data.get("imgname")
                print(img_name)
                de_img = io.BytesIO(base64.b64decode(image))
                img = Image.open(de_img)
                byte_size = int(len(img.fp.read()))
                
                print(byte_size)

#                        descrpt = read_image(img)
                print(img.verify())
                return resp.accepted("image saved")
            
"""
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
            
    except:
        return resp.not_found("image album not found")

"""