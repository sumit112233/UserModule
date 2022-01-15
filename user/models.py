from django.db import models

class User(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     email = models.EmailField()
     password = models.CharField(max_length=50)
     username = models.CharField(max_length=50)

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
