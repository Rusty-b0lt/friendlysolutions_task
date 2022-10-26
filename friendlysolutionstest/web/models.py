import os

from django.db import models

# Create your models here.
from django.dispatch.dispatcher import receiver


class Image(models.Model):
    title = models.CharField(max_length=255)
    album_id = models.IntegerField() # I thought it should be a ForeignKey field, but I'll leave it an IntegerField for now
    width = models.IntegerField()
    height = models.IntegerField()
    color = models.CharField(max_length=7)
    file = models.ImageField(upload_to='images/', height_field='height', width_field='width', null=False)
