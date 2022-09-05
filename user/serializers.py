from rest_framework import serializers,validators
from .models import User

class UserSerializer(serializers.ModelSerializer):
    date_joined=serializers.DateTimeField(read_only=True)
    class Meta:
        model=User
        fields=['id','username','email','date_joined','password']
        extra_kwargs={
            'username':{'required':True,'validators':[validators.UniqueValidator(User.objects.all())]},
            'password':{'required':True,'write_only':True,}
        }
class LoginSerializer(serializers.ModelSerializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['id','username','password']