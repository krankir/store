from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Расширенная модель пользователя."""

    image = models.ImageField(upload_to='users_images', blank=True, null=True)
