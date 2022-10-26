import requests
from django.core.management.base import BaseCommand, CommandError

from friendlysolutionstest.api.helpers import import_from_json, parse_json


class Command(BaseCommand):
    help = 'Imports images from external api'

    def add_arguments(self, parser):
        parser.add_argument('albumId', type=int, help='Indicates images from which album to import')


    def handle(self, *args, **options):
        json = requests.get('https://jsonplaceholder.typicode.com/photos').content
        data = parse_json(json)
        data = [d for d in data if d['albumId'] == options['albumId']]
        if len(data) == 0:
            print('No album with this id!')
        else:
            import_from_json(data)