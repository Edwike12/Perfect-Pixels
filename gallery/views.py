from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from gallery.forms import ImageForm
from .models import *

# Create your views here.
def index(request):
   categories = Category.objects.all()
   locations = Location.objects.all()
   if 'category' in request.GET and request.GET["category"]:
        category_id = request.GET.get("category")
        post = Image.objects.filter(category = category_id)
        
   elif 'location' in request.GET and request.GET["location"]:
        location_id = request.GET.get("location")
        post = Image.objects.filter(location = location_id)
       
   else:
        post = Image.objects.all()

   context={'post':post, 'categories': categories, 'locations':locations}
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


def search_results(request):

    if 'images' in request.GET and request.GET["images"]:
        search_term = request.GET.get("images")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def location(request, location_id):
    locations = Location.objects.all()
    images = Image.objects.filter(location_id=location_id)
    location = Location.objects.get(id=location_id)
    title = location
    return render(request, 'location.html', {'images': images, 'locations': locations, 'title': title})   

def images(request,images_id):
    try:
        images = Image.objects.get(id = images_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"all-pics/images.html", {"images":images})         
   


    