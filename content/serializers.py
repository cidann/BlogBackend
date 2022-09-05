from rest_framework import serializers
from .models import Blog
class BlogSerializer(serializers.ModelSerializer):
    time=serializers.DateTimeField(format="%d %B, %Y %I:%M %p",required=False)
    user=serializers.SlugRelatedField(read_only=True,slug_field='username')
    class Meta:
        model=Blog
        fields='__all__'
