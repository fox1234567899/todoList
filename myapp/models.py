from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=models.ImageField(upload_to='avatars/',default='6596121.png')

    def __str__(self):
        return self.user.username
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
    


