from rest_framework import serializers
from . models import language, paradigm,programmer


class languageSerializer(serializers.ModelSerializer):
    class Meta:
        model = language
        fields =('id','name','paradigm')

class paradigmSerializer(serializers.ModelSerializer):
    class Meta:
        model = paradigm
        fields = ('id','name')
class programmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        fields = ('id','name','language')