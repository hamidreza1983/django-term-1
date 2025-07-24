from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=11)
    id_code = models.CharField(max_length=10)

    