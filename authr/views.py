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
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from authr.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

UserModel = get_user_model()


@api_view(["post"])
@permission_classes([AllowAny])
def UserCreateView(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")
        last_name = request.data.get("last_name")
        first_name = request.data.get("first_name")
        email = request.data.get("email")
        if (
            UserModel.objects.filter(username__icontains=username).first()
            or UserModel.objects.filter(email=email).first()
        ):
            return Response(
                {
                    "status": False,
                    "message": "username or email address already taken by another user ",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
        else:
            data = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "username": username,
                "password": password,
            }
            serializer_class = UserSerializer(data=data)
            serializer_class.is_valid(raise_exception=True)
            data = serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_201_CREATED)


@api_view(["post"])
def authr_token(request):
    if request.method == "POST":
        account_name = request.data.get("username")
        password = request.data.get("password")
        try:
            log = authenticate(account_name=account_name, password=password)
            refresh = RefreshToken.for_user(log)
            return Response(
                {
                    "responsecode": 200,
                    "success": True,
                    "accesstoken": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        except AttributeError:
            return Response(
                {
                    "responsecode": 401,
                    "success": False,
                    "message": "Please enter the correct username and password",
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )
