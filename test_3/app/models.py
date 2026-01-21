"""Models for test application."""

from django.db import models
from django.contrib.auth.models import AbstractUser

class AppUser(AbstractUser):
    roll_no = models.IntegerField(default=0,blank=True,null=True)
    def __str__(self) -> str:
        return str(self.id)
    
class TestModel(models.Model):
    """Model representing a test entity."""

    roll_no = models.IntegerField(default=0, blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.name)
    