from django.shortcuts import render
from django.http import Http404
from rest_framework import generics,decorators,mixins,permissions,parsers
from .models import *
from .serializers import BlogSerializer
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from blog.authentication import SafeTokenAuthentication
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
# Create your views here.

def index(request):
    render(request,'blogfrontend/public/index.html')

class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.prefetch_related('user')
    serializer_class = BlogSerializer
    authentication_classes = [SafeTokenAuthentication,]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        filter=self.request.query_params.get('filter','')
        return self.queryset.filter(title__icontains=filter)


class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    authentication_classes = [SafeTokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


