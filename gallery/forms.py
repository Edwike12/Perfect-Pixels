from .models import *
from django.db.models import fields
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:

        model=Image
        fields=['image', 'name', 'description']
