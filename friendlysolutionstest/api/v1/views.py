import json

import requests
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from friendlysolutionstest.api.helpers import parse_json, import_from_json
from friendlysolutionstest.web.models import Image
from friendlysolutionstest.api.v1.serializers import ImageCreateUpdateSerializer, ImageListSerializer, \
ImageImportFromApiSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageCreateUpdateSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ImageListSerializer
        else:
            return self.serializer_class

    @action(detail=False, methods=['post'], serializer_class=ImageImportFromApiSerializer)
    def import_from_api(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        json = requests.get('https://jsonplaceholder.typicode.com/photos').content
        data = parse_json(json)
        data = [d for d in data if d['albumId'] == serializer.validated_data['albumId']]
        if len(data) == 0:
            return Response({'detail': 'No album found with this id.'}, status=status.HTTP_400_BAD_REQUEST)
        num = import_from_json(data)
        return Response({'detail': f'Successfully imported {num} images.'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def import_from_file(self, request):
        if len(request.data) == 0:
            return Response({'detail': 'Empty file.'}, status=status.HTTP_400_BAD_REQUEST)
        num = import_from_json(request.data)
        return Response({'detail': f'Successfully imported {num} images.'}, status=status.HTTP_201_CREATED)