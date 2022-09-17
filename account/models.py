from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        if not name:
            raise ValueError(_("User must have a name"))
        if password is None:
            raise ValueError(_("Users must have a Password"))
        user = self.model(email=self.normalize_email(email), name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)
        if not extra_fields.get("is_staff"):
            raise ValueError(_("staff must be set to true"))
        if not extra_fields.get("is_superuser"):
            raise ValueError(_("Superuser must be set to true"))
        user = self.create_user(email, name, password, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # User Basic Details
    email = models.EmailField(_("Email"), max_length=100, unique=True, db_index=True)
    name = models.CharField(_("name"), max_length=15)

    # User status
    is_seller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}
