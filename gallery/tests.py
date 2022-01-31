from django.test import TestCase
from gallery.models import Location, Category, Image


class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a location for testing
        """
        Location.objects.create(name="Test Location")

    def test_location_name(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(name="Test Location")
        self.assertEqual(location.name, "Test Location")

    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(name="Test Location")
        self.assertEqual(str(location), "Test Location")

class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="Test Category")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_category_str(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(str(category), "Test Category")


# class ImageTestCase(TestCase):
#     def setUp(self):
#         """
#         Create a image for testing
#         """
#         Image.objects.create(
#             name="Test images",
#             description="Test Description",
#             location=Location.objects.create(name="Image Location"),
#             category=Category.objects.create(name="Image Category"),
#         )
#     def test_images_name(self):
#         """
#         Test that the image name is correct
#         """
#         image = Image.objects.get(name="Test image")
#         self.assertEqual(image.name, "Test image")
#     def test_images_description(self):
#         """
#         Test that the image description is correct
#         """
#         image = Image.objects.get(name="Test image")
#         self.assertEqual(image.description, "Test Description")
#     def test_images_location(self):
#         """
#         Test that the image location is correct
#         """
#         image = Image.objects.get(name="Test image")
#         self.assertEqual(image.location.name, "image Location")
#     def test_images_category(self):
#         """
#         Test that the image category is correct
#         """
#         image = Image.objects.get(name="Test image")
#         self.assertEqual(image.category.name, "image Category")
#     def test_images_str(self):
#         """
#         Test that the image string representation is correct
#         """
#         image = Image.objects.get(name="Test image")
#         self.assertEqual(str(image), "Test image")

