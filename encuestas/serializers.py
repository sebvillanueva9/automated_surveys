from rest_framework import serializers

class ResultadosSerializer(serializers.Serializer):
    tablas = serializers.CharField()
    grafico = serializers.CharField()
