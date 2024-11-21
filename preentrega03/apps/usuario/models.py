from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email= models.EmailField(unique=True,null=False,blank=False)
    avatar = models.ImageField(upload_to="usuarios/", default= "../static/avatardef.jpg")
    
    def delete(self, using = ..., keep_parents = ...):
        if self.avatar.name != "../static/avatardef.jpg":
            self.avatar.delete (self.avatar.name)
        return super().delete()
    
# Create your models here.
