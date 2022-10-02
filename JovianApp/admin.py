from django.contrib import admin

from .models import Images
from .models import Gallery

# Register your models here.

admin.site.register(Images)
admin.site.register(Gallery)