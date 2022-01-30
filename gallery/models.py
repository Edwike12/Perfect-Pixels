from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
# class location
# class category
# class image
class Image(models.Model):
    image=CloudinaryField('Image')
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
