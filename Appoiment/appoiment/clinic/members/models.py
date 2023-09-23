from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER=(
        ('1','Doctor'),
        ('2','Patient'),

    )
    user_type = models.CharField(choices=USER, max_length=20, default=2)


class Doctor(models.Model):
    admin  = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    doc_phone = models.IntegerField()
    doc_education = models.CharField(max_length=50)
    doc_age = models.PositiveIntegerField()
    doc_specialist = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.admin.username