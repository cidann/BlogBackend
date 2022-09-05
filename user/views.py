import django.shortcuts
from rest_framework import generics
from rest_framework import views,response
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.authtoken.models import Token
from blog.authentication import SafeTokenAuthentication
from user.models import User
from user.serializers import UserSerializer,LoginSerializer
from django.contrib.auth import login,authenticate
from django.views.decorators.csrf import csrf_exempt
from user.permissions import UserPermission
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [SafeTokenAuthentication]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=User.objects.create_user(username=request.data['username'],password=request.data['password'])
        token=Token.objects.create(user=user)
        headers = self.get_success_headers(serializer.data)
        data={'user':serializer.data,'token':token.key}
        return response.Response(data, status=201, headers=headers)



class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [UserPermission]
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]

class UserLogin(generics.GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = [SafeTokenAuthentication]
    def get(self, request, *args, **kwargs):
        if(self.request.user.is_authenticated):
            serializer=self.get_serializer(self.request.user)
            return response.Response({'success':serializer.data}, 200)
        else:
            return response.Response({'error':f'not authenticated'},200)
    def post(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            user=authenticate(username=request.data['username'],password=request.data['password'])
            if(user):
                exist=Token.objects.filter(user=user).first()
                if(exist):
                    exist.delete()
                token=Token.objects.create(user=user)
                return response.Response({'success': {
                    'token':token.key,
                    'user':{
                        'username':user.username,
                        'id':user.id
                    }
                }},200)
        return response.Response({'error':f'invalid username or password'},200)


