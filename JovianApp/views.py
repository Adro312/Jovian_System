from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Galery, Images
from .forms import ImagesForm
from .algoritm import giveColor

# Create your views here.
def home(request):
    return render(request, "pages/index.html")

def galery(request):
    images = Galery.objects.all()
    return render(request, "pages/galery.html", {'images': images})

def about_us(request):
    return render(request, "pages/about-us.html")

def process(request):
    # Get model's fields
    form = ImagesForm(request.POST or None, request.FILES or None)

    # Save images
    if form.is_valid():
        # save images
        form.save()

        # get last ID
        imgsID = Images.objects.latest('id')

        # get paths of last Id
        imgs = Images.objects.get(id=imgsID.id)

        # give color
        img = giveColor(imgs.redImage, imgs.greenImage, imgs.blueImage, imgsID.id)

        # save in the db
        Galery.objects.create(
            image = img
        )

        # get last ID
        imgsGalleryID = Galery.objects.latest('id')

        # get paths of last Id
        imgsGallery = Galery.objects.get(id=imgsGalleryID.id)

        # reditect to edit image
        return render(request, "pages/image.html", {'colored_Img': imgsGallery})

    return render(request, "pages/process.html", {'form': form})

def image(request):
    return render(request, "pages/image.html")