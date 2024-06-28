from rest_framework.serializers import ModelSerializer
from datetime import datetime
class BaseSerializer(ModelSerializer):

    def create(self,validated_data):
        validated_data['created_by'] = self.context['request'].user.username
        
        return super().create(validated_data)

    def validate(self, validated_data):
        if self.context['request'].method == "POST":
            validated_data['created_by'] = self.context['request'].user.username

        if self.context['request'].method in ("PUT","PATCH"):
            validated_data['updated_by'] = self.context['request'].user.username
            validated_data['updated_at'] = datetime.now()
        return validated_data