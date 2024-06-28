from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from base.authorization import CustomAuthentication
from rest_framework.response import Response
from .models import User,Data
from .serializers import UserSerializer,DataSerializer
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timedelta
import jwt

class UserModelViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # parser_classes = [MultiPartParser, FormParser]

 
class UserLogin(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):

        user = authenticate(**request.data)
       
        try:
            payload = {"user_id":user.id}
            payload['exp'] = datetime.utcnow() + timedelta(minutes=1)
            #payload['exp'] = int(payload['exp'].timestamp())
            token = jwt.encode(payload,'abcd',algorithm='HS256')
            return Response({'token': token},status=status.HTTP_201_CREATED)
        
        except Exception as error:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        
class UserDataViewSet(ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Data.objects.all()
    serializer_class = DataSerializer 

    

    
    



        
       

