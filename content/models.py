from django.db import models
from user.models import User
from django.core.validators import validate_image_file_extension
import os
from dotenv import load_dotenv
load_dotenv()
# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog')
    title=models.TextField()
    image=models.ImageField(
        upload_to=os.path.join(os.environ.get('DEVELOPMENT','production'),'blog/image'),
        default='default.PNG',
        validators=[validate_image_file_extension]
    )
    content=models.TextField()
    time=models.DateTimeField(auto_now_add=True)


