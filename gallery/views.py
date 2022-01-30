from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from gallery.forms import ImageForm
from .models import *

# Create your views here.
def index(request):
   post=Image.objects.all()

   context={'post':post}
   return render(request, 'index.html',context)

def add_image(request):
   
   if request.method=='POST':
      form = ImageForm (request.POST , request.FILES)
      if form.is_valid():
            form.instance.user = request.user
            form.save()
      return HttpResponseRedirect('/') 
   else:
      form=ImageForm()
   return render(request, 'add_image.html',{'form':form})
    