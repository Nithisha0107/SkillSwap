from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SkillCategory,Skill
from .serializers import CategorySerializer,SkillSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CategoryViewset(ModelViewSet):
    #authentication_classes = []
    #permission_classes = []
    queryset= SkillCategory.objects.all()
    serializer_class = CategorySerializer

class SkillViewSet(ModelViewSet):
    
    queryset  = Skill.objects.all()
    serializer_class = SkillSerializer


