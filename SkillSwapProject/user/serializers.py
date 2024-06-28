from rest_framework.serializers import ModelSerializer, ValidationError
from .models import User,Data
from base.serializers import BaseSerializer
from datetime import datetime

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'password', 'email', 'phone_number', 'qualification', 'occupation', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}
        

    

    def create(self, validated_data):
        profile_picture = validated_data.pop('profile_picture', None)
        user = User.objects.create_user(**validated_data)
        if profile_picture:
            user.profile_picture = profile_picture
            user.save()
        return user
    
class DataSerializer(BaseSerializer):
    #import pdb;pdb.set_trace()
  
    class Meta:
        model = Data
        fields = "__all__"
       
        db_index = True
    
    
    
    

    