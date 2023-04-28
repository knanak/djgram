from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    Gender=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custom')
    ]

    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    user_name = models.CharField(max_length=255,blank=True )
    profile_photo = models.ImageField(blank=True)
    desc=models.TextField(max_length=400, blank=True)
    gender=models.CharField(choices=Gender, max_length=100, blank=True)

    followers=models.ManyToManyField("self")
    following=models.ManyToManyField("self")

    def get_absolute_url(self) -> str:

        return reverse("users:detail", kwargs={"username": self.username})
