from rest_framework import serializers
from account.models import User
from apikey.models import Keys
from apikey.key_gen import all_key

UserModel = User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        email = validated_data["email"]
        apikeys = all_key(email)

        user = UserModel.objects.create_user(
            email=email,
            name=validated_data["name"],
            password=validated_data["password"],
        )

        Keys.objects.create(user = user,
            public_key = apikeys[0],
            private_key = apikeys[1],
            enc_public_key = apikeys[2],
            enc_private_key = apikeys[3])
        return user

    class Meta:
        model = User
        fields = ["name", "email", "password"]
