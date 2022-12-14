from django.shortcuts import render, HttpResponse
from box.models import Folder, UserStorageVolume
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from box.serializers import FolderSerial
from box.hash import hashes
from folderapp import resp


# To create album and display all album created
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def index(request):
    user = request.user

# Post request to create new image album
    if request.method == "POST":
        folder_name = request.data.get("name")
        code = hashes()
        visible = request.data.get("visible")
        anyone_upload = request.data.get("anyone_upload")
        data = Folder.objects.create(
            user=user,
            folder_name=folder_name,
            visible=visible,
            code=code,
            anyone_upload=anyone_upload,
        )
        serializer_class = FolderSerial(data)
        return Response(serializer_class.data, status=status.HTTP_201_CREATED)

# Get request to display all image album created
    else:
        folder = Folder.objects.filter(user=user)
        serializer_class = FolderSerial(folder, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)


# Function to delete and update image album
@api_view(["DELETE", "PUT"])
@permission_classes([IsAuthenticated])
def delete_folder(request, code):
    current_user = request.user

# Delete request to delete an image album
    if request.method == "DELETE":
        try:
            del_folder = Folder.objects.get(code=code)
            if del_folder.user == current_user:
                del_folder.delete()
                return resp.it_ok("album deleted")
            else:
                return resp.not_yours("not your account")
        except Folder.DoesNotExist:
            return resp.not_found("album not found")

# Put request to update image album visibility and who can upload
    if request.method == "PUT":
        visible = request.data.get("visible")
        print(visible)
        who_upload = request.data.get("anyone_upload")
        print(who_upload)
        if visible == "" and who_upload == True or who_upload == False:
            try:
                visible_update = Folder.objects.get(code=code)
                if visible_update.user == current_user:
                    visible_update.anyone_upload = who_upload
                    visible_update.save()
                    return resp.it_ok({"anyone_upload": who_upload})
                else:
                    return resp.not_yours("not your account")
            except:
                return resp.not_found("album not found")

        if who_upload == "" and visible == True or visible == False:
            try:
                upload_update = Folder.objects.get(code=code)
                if upload_update.user == current_user:
                    upload_update.visible = visible
                    upload_update.save()
                    return resp.it_ok({"visible": visible})
                else:
                    return resp.not_yours("not your account")
            except:
                return resp.not_found("album not found")
        else:
            return resp.bad("wrong data")
