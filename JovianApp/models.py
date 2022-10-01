from django.db import models

# Create your models here.
class Images(models.Model) :
    id = models.AutoField(primary_key = True)
    redImage = models.ImageField(upload_to = 'images/red_img/', verbose_name = 'Red_Image', null = True)
    greenImage = models.ImageField(upload_to = 'images/green_img/', verbose_name = 'Green_Image', null = True)
    blueImage = models.ImageField(upload_to = 'images/blue_img/', verbose_name = 'Blue_Image', null = True)

    def delete(self, using = None, keep_parents = False):
        self.redImage.storage.delete(self.redImage.name)
        self.greenImage.storage.delete(self.greenImage.name)
        self.blueImage.storage.delete(self.blueImage.name)
        super().delete()

class Galery(models.Model) :
    id = models.AutoField(primary_key = True)
    image = models.ImageField(upload_to = 'images/galery/', null = True)

    def delete(self, using = None, keep_parents = False):
        self.image.storage.delete(self.image.name)
        super().delete()