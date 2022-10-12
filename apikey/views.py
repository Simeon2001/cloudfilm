from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from .models import Keys
from folderapp import resp
from .key_gen import all_key
from apikey.microreq import putkey


@api_view(["get", "put"])
@permission_classes([IsAuthenticated])
def get_apikey(request):
    current_user = request.user
    if request.method == "PUT":
        user_email = current_user.email
        up_apikey = all_key(user_email)
        try:
            update_keys = Keys.objects.get(user=current_user)

            key_status = putkey(update_keys.enc_private_key, up_apikey[3], up_apikey[2])

            update_keys.public_key = up_apikey[0]
            update_keys.private_key = up_apikey[1]
            update_keys.enc_public_key = up_apikey[2]
            update_keys.enc_private_key = up_apikey[3]
            
            if key_status == 200:
                update_keys.save()

                return Response(
                    {
                        "status": True,
                        "secret_key": up_apikey[1],
                        "public_key": up_apikey[0],
                    },
                    status=status.HTTP_201_CREATED,
                )

            else:
                return Response(
                    {
                        "status": False,
                        "msg": "something is wrong",
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        except:
            return resp.not_found("user not found")

    else:
        try:
            keys = Keys.objects.get(user=current_user)
            return Response(
                {
                    "status": True,
                    "secret_key": keys.private_key,
                    "public_key": keys.public_key,
                },
                status=status.HTTP_200_OK,
            )
        except:
            return resp.not_found("user not found")
