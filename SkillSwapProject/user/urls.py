from rest_framework.routers import DefaultRouter 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import UserModelViewSet

router = DefaultRouter()

router.register(r'user',UserModelViewSet,basename='user')


urlpatterns = [path('', include(router.urls))
               ]
