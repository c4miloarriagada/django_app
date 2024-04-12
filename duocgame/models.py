from django.db import models
from django.contrib.auth import get_user_model
from djangoapp import settings 

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    role = models.CharField(max_length=25, choices=settings.ROLES)
    def __str__(self):
        return self.user.username + " - " + self.role + " - " + str(self.user.id)

