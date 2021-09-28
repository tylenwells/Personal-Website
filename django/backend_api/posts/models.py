from django.db import models
from django.http import JsonResponse
# Create your models here.


class Post(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=1000)
    timetoread = models.TextField(max_length=20)
    content = models.TextField()

    def __jsonify__(self):
        return JsonResponse({
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "timetoread": self.timetoread,
            "content": self.content
        })
