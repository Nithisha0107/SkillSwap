from .models import User
from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError

class Userserializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','first_name','last_name','username','password','email','phone_number','qualification','occupation','profile_picture']

        def validate(self, validated_data):
            if not (validated_data.get("first_name").isalpha() or validated_data.get("last_name").isalpha()):
                raise ValidationError("Please enter valid name")
            
            # if (validated_data.get("first_name") == '' or validated_data.get("last_name") == ''):
            #     raise ValidationError('This field may not be blank.')
            validated_data['first_name'] = validated_data['first_name'].upper()
            validated_data['last_name'] = validated_data['last_name'].upper()

            return super().validate()