from django.db import models

# Create your models here.
class Rcp(models.Model):
    uname = models.CharField(max_length=100)
    Rname = models.CharField(max_length=100)
    Ingredients = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Rcp_Images/', blank=True)
    steps = models.CharField(max_length=1000)    

    def __str__(self):
        return self.uname