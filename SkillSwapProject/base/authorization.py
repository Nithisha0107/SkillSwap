
from rest_framework import exceptions
import jwt
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from django.core.cache import cache
from rest_framework.response import Response
class CustomAuthentication(TokenAuthentication):

    def authenticate_credentials(self, key):

        try:
            # user = cache.get(key)
            # print("cache user")
            #if not user:
                payload = jwt.decode(key,'abcd',algorithms='HS256')
                print(payload)
                user = get_user_model().objects.get(id = payload.get('user_id'))
                # print('db user')
                # cache.set(key, user, timeout=3600)
            
        # except jwt.ExpiredSignatureError:
        #     return "Token has expired"
        # except jwt.InvalidTokenError:
        #     return "Invalid token"
        except Exception as error:
            raise exceptions.AuthenticationFailed("Invalid Token")
        return (user, key)