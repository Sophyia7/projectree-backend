from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from accounts.managers import CustomUserManager


# Create your User Model here.
class User(AbstractBaseUser, PermissionsMixin):
    # Abstractbaseuser has password, last_login, is_active by default

    username = models.CharField(max_length=90, null=True)
    email = models.EmailField(db_index=True, unique=True, max_length=254, null=True)
    first_name = models.CharField(max_length=240, null=True)
    last_name = models.CharField(max_length=255, null=True)

    is_staff = models.BooleanField(
        default=True
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_active = models.BooleanField(
        default=True
    )  # must needed, otherwise you won't be able to loginto django-admin.
    is_superuser = models.BooleanField(
        default=False
    )  # this field we inherit from PermissionsMixin.

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
