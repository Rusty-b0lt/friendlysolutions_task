import os
from django.db import models
from django.dispatch.dispatcher import receiver

from friendlysolutionstest.web.models import Image

def delete_file(path):
   """ Deletes file from filesystem. """
   if os.path.isfile(path):
       os.remove(path)
       print('deleted')

@receiver(models.signals.post_delete, sender=Image)
def delete_image(sender, instance, *args, **kwargs):
    print('signal')
    """ Deletes thumbnail files on `post_delete` """
    if instance.file:
        delete_file(instance.file.path)