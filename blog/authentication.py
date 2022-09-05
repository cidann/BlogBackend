from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
class SafeTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except:
            return None
