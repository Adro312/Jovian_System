from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Galery
from .forms import ImagesForm

# Create your views here.
def home(request):
    return render(request, "pages/index.html")

def galery(request):
    galery = Galery.objects.all()
    return render(request, "pages/galery.html", {'galery': galery})

def about_us(request):
    return render(request, "pages/about-us.html")

def process(request):
    # Get model's fields
    form = ImagesForm(request.POST or None, request.FILES or None)

    # Save images
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "pages/process.html", {'form': form})