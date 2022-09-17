from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from account.models import User
from django.contrib.auth import get_user_model
from account.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from folderapp import resp

UserModel = get_user_model()


@api_view(["post"])
@permission_classes([AllowAny])
def usercreateview(request):
    if request.method == "POST":
        name = request.data.get("name")
        password = request.data.get("password")
        email = request.data.get("email")
        if UserModel.objects.filter(email=email).first():
            return resp.bad("email address already taken by another user")

        else:
            data = {
                "name": name,
                "email": email,
                "password": password,
            }
            serializer_class = UserSerializer(data=data)
            serializer_class.is_valid(raise_exception=True)
            data = serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)


@api_view(["post"])
def authr_token(request):
    if request.method == "POST":
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            log = authenticate(email=email, password=password)
            refresh = RefreshToken.for_user(log)
            return Response(
                {
                    "status": True,
                    "accesstoken": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        except AttributeError:
            return resp.bad("Please enter the correct email address and password")
