from email.policy import default
from django.db import models

# Create your models here.

"""
class Post:
    title: str
    author: str
    content: str
    thumbnail: image
"""

class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='posts/static/img/thumbnails', default='default.png')
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'<Post {self.title}>'
