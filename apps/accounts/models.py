from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    birthday = models.DateField(blank=True, null=True)
