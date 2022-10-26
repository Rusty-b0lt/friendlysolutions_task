from rest_framework import serializers
from friendlysolutionstest.web.models import Image
from friendlysolutionstest.api.helpers import get_dominant_color, download_image
from friendlysolutionstest.web.signals import delete_file


class ImageCreateUpdateSerializer(serializers.ModelSerializer):

    albumId = serializers.IntegerField(source='album_id')
    url = serializers.URLField(write_only=True, required=True)

    def create(self, validated_data):
        print('create')
        if 'url' in validated_data:
            # downloading image
            file = download_image(validated_data.pop('url'))
            validated_data['file'] = file
        print(validated_data)
        instance = super().create(validated_data)
        dom_color = get_dominant_color(instance.file.path)
        instance.color = dom_color
        instance.save()
        return instance

    def update(self, instance, validated_data):
        if 'url' in validated_data:
            # downloading image
            file = download_image(validated_data.pop('url'))
            validated_data['file'] = file
            # finding dominant color
            dom_color = get_dominant_color(file)
            validated_data['color'] = dom_color
            # deleting old image
            delete_file(instance.file.path if instance.file else None)
        instance = super().update(instance, validated_data)
        return instance

    class Meta:
        model = Image
        fields = ['id', 'title', 'albumId', 'url', 'file']
        extra_kwargs = {'file': {'read_only': True}}


class ImageListSerializer(ImageCreateUpdateSerializer):

    class Meta:
        model = Image
        fields = ['id','title', 'albumId', 'file', 'height', 'width', 'color']


class ImageImportFromApiSerializer(serializers.Serializer):
    albumId = serializers.IntegerField()