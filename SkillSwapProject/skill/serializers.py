from .models import SkillCategory,Skill
from rest_framework.serializers import ModelSerializer
from datetime import datetime
from base.serializers import BaseSerializer
class CategorySerializer(ModelSerializer):

    class Meta:
        model = SkillCategory
        fields = "__all__"

class SkillSerializer(BaseSerializer):

    class Meta:
        model = Skill
        fields = "__all__"
       

    
    



