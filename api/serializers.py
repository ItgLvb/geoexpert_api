from rest_framework import serializers
from .models import CadastralPlot


class CadastralPlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastralPlot
        fields = ('cadastral_number', 'short_cadastral_number', 'geometry', 'address')
