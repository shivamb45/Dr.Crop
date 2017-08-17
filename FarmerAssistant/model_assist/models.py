from django.db import models
from FarmerAssistant.settings import BASE_DIR
import os
from analyzer.label_image import returnImageStat

# Create your models here.

class SubmittedImage(models.Model):
    image = models.ImageField(null=True)
    path = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.image.name

    def save(self,*args,**kwargs):
        print(self.image.path)

        self.path = self.image.path
        # print(returnImageStat(self.path))
        # self.save()
        super(SubmittedImage,self).save()

class ImageClass2(models.Model):
    image = models.ImageField(null=True)
    path = models.TextField(blank=True,null=True)
