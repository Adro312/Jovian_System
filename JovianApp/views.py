from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gallery, Images
from .forms import ImagesForm
from .deploy import giveColor

# Create your views here.
def home(request):
    return render(request, "pages/index.html")

def gallery(request):
    images = Gallery.objects.all()
    return render(request, "pages/gallery.html", {'images': images})

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
        img = giveColor(imgs.redImage, imgs.greenImage, imgs.blueImage, imgs.mapProjected, imgsID.id)

        # save in the db
        Gallery.objects.create(
            image = img
        )

        # get last ID
        imgsGalleryID = Gallery.objects.latest('id')

        # get paths of last Id
        imgsGallery = Gallery.objects.get(id=imgsGalleryID.id)

        # filters
        filters = ['soft_light', 'dodge', 'lighten_only', 'addition', 'darken_only', 'multiply', 'hard_light', 'difference', 'grain_merge', 'overlay', 'normal']

        # reditect to edit image
        return render(request, "pages/image.html", {
            'colored_Img': imgsGallery,
            'imgID' : imgsGalleryID,
            'filters': filters,
        })

    return render(request, "pages/process.html", {'form': form})

def image(request):
    return render(request, "pages/image.html")