from rest_framework import serializers
from . import models


class ImgMriSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'examen', 'url')
        model = models.ImgMri