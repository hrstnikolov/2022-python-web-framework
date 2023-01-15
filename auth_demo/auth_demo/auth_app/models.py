from django.contrib.auth import models as auth_models
from django.db import models

from auth_demo.auth_app.managers import AppUserManager


# class CustomUser(auth_models.User):
#     def has_email(self):
#         return self.email or False
#
#     class Meta:
#         proxy = True


class MyUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )
    is_staff =models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    USERNAME_FIELD = "email"

    object = AppUserManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )
    last_name = models.CharField(
        max_length=25,
    )
    age = models.PositiveIntegerField()

    user = models.OneToOneField(
        to=MyUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )