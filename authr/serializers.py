from rest_framework import serializers
from django.contrib.auth.models import User

UserModel = User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8,write_only=True)

    def create(self, validated_data):
        username = validated_data["username"]
        
        user = UserModel.objects.create_user(
            username=username,
            email=validated_data["email"],
            last_name=validated_data["last_name"],
            first_name=validated_data["first_name"],
            password =validated_data["password"],
        )
        return user

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "password"]