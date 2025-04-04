from rest_framework import serializers
from . import models


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'fecha', 'historiaPaciente', 'especialidad', 'comentarios')
        model = models.Evento