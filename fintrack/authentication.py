import jwt
from django.conf import settings
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import AnonymousUser
from types import SimpleNamespace

class NodeJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')

        if not auth_header or not auth_header.startswith("Bearer "):
            return None 

        token = auth_header.split(" ")[1]
        
        try:    
            decoded = jwt.decode(token, settings.JWT_SECRET, algorithms=["HS256"])
            user = SimpleNamespace(
                is_authenticated=True,
                id=decoded.get("userId"),
                email=decoded.get("email"),
                role=decoded.get("role")
            )

            return (user, None)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Token has expired")
        except jwt.InvalidTokenError:
            raise AuthenticationFailed("Invalid token")