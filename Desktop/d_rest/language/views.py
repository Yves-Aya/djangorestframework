from django.shortcuts import render
from rest_framework import viewsets
from . models import language,paradigm,programmer
from . serializers import languageSerializer,paradigmSerializer,programmerSerializer

# Create your views here.
class languageView(viewsets.ModelViewSet):
    queryset = language.objects.all()
    serializer_class = languageSerializer

class paradigmView(viewsets.ModelViewSet):
    queryset =paradigm.objects.all()
    serializer_class = paradigmSerializer


class programmerView(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = programmerSerializer
