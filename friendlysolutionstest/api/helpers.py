import requests
from io import BytesIO
from rest_framework.parsers import JSONParser
import PIL

from django.conf import settings
from django.core.files.images import ImageFile
from colorthief import ColorThief

from friendlysolutionstest.web.models import Image


def download_image(url):
    img_data = requests.get(url).content
    img_file = ImageFile(BytesIO(img_data), name=url.split('/')[-1])
    return img_file

def download_image_to_folder(url):
    filename = url.split('/')[-1]
    img_data = requests.get(url).content
    img = PIL.Image.open(BytesIO(img_data))
    img.save(settings.MEDIA_ROOT + 'images/' + filename, format='png')
    return {'filename': 'images/' + filename, 'width': img.width, 'height': img.height}

# Might move to async celery task
def get_dominant_color(image_path):
    color_thief = ColorThief(image_path)
    dominant_color = color_thief.get_color()
    dom_color_hex = '#%02x%02x%02x' % dominant_color
    return dom_color_hex

def parse_json(json):
    stream = BytesIO(json)
    data = JSONParser().parse(stream)
    return data

def import_from_json(data):
    from friendlysolutionstest.api.v1.serializers import ImageCreateUpdateSerializer
    objs = []
    serializer = ImageCreateUpdateSerializer(data=data, many=True)
    serializer.is_valid(raise_exception=True)
    print('Starting download...')
    for index, image in enumerate(serializer.validated_data):
        img = download_image_to_folder(image.pop('url') + '.png')
        obj = Image(**image)
        obj.file.name = img['filename']
        dom_color = get_dominant_color(obj.file.path)
        obj.color = dom_color
        obj.width = img['width']
        obj.height = img['height']
        objs.append(obj)
        print(f'Finished downloading image number {index + 1}.')
    Image.objects.bulk_create(objs)
    print('Created database objects.')
    return len(objs)
