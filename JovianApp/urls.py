from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.home, name='inicio'),
    path('galery', views.galery, name='galery'),
    path('about-us', views.about_us, name='about-us'),
    path('process', views.process, name='process'),
    path('image', views.image, name='image'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
