
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.
class FacebookPosts(models.Model):
    post_data = models.CharField(max_length=10000)
    post_date = models.DateTimeField()
    
    