from rest_framework import serializers
from model_assist.models import SubmittedImage,ImageClass2

class SubmittedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmittedImage
        read_only_fields = ('path',)

class ImageClass2Serializer(serializers.ModelSerializer):
    class Meta:
        model = ImageClass2
        
