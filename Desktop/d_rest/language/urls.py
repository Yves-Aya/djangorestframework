from django.urls import path,include
from . import  views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('language', views.languageView)
router.register('paradigm',views.paradigmView)
router.register('programmer',views.programmerView)
urlpatterns = [
    path('',include(router.urls))


]
