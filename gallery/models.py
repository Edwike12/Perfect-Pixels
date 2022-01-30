from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40, null=True)

    
    def save_category(self):
        self.save()

    
    def update_category(self, name):
        self.name = name
        self.save()

    
    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=40, null=True)

    
    def save_location(self):
        self.save()

    
    def update_location(self, name):
        self.name = name
        self.save()

    
    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name
# class image
class Image(models.Model):
    image=CloudinaryField('Image')
    name=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def save_image(self):
        self.save()


    # update image
    def update_image(self, name, description):
        self.name = name
        self.description = description
        # self.location = location
        self.category = Category
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        post = cls.objects.filter(category__name__icontains=search_term)
        return post

    @classmethod
    def filter_by_location(cls,search_location):
        location = cls.objects.filter(location__name__=search_location).all()
        return location

    def delete_image(self):
        self.delete()

    @classmethod
    def search(cls, search_term):
        images_by_category = cls.filter_by_category(search_term)
        images_by_location = cls.filter_by_location(search_term)
        return images_by_category.union(images_by_location)

    def __str__(self):
        return self.name



   
