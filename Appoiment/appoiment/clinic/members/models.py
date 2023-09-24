from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=(
        (1,'Doctor'),
        (2,'Patient'),

    )
    user_type = models.CharField(choices=USER, max_length=20, default=1)