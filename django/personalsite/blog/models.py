from django.db import models
from django.http import JsonResponse


# Create your models here.


class User(models.Model):
    firstname = models.TextField(max_length=50)
    lastname = models.TextField(max_length=50)
    email = models.EmailField()


class Post(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    timetoread = models.TextField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
