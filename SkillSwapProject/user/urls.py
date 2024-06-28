from rest_framework.routers import DefaultRouter 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import UserModelViewSet,UserLogin,UserDataViewSet

router = DefaultRouter()

router.register(r'userregister',UserModelViewSet,basename='user')
router.register(r'data',UserDataViewSet,basename='data')


urlpatterns = [path('login/',UserLogin.as_view(),name='data')]+router.urls
    #path('', include(router.urls)),
               
