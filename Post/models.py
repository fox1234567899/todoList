from django.db import models
from django.contrib.auth.models import User 


class MyPost(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=300,blank=True,null=True)
    image=models.ImageField(blank=True,null=True,upload_to="images/")
    time=models.DateTimeField(blank=True,null=True)
    user=models.ForeignKey(User,models.CASCADE)
    checked=models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering=['checked']