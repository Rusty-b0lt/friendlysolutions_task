from io import BytesIO
import json
from django.core.management.base import BaseCommand, CommandError
import argparse

from friendlysolutionstest.api.helpers import import_from_json

class Command(BaseCommand):
    help = 'Imports images from external api'

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'), help='Json file to open')

    def handle(self, *args, **options):
        data = json.load(options['file'])
        import_from_json(data)
