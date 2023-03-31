from django.db import models

# Create your models here.

class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.TextField()
    slug = models.CharField(max_length=500)
    date = models.DateTimeField(blank=True)
    views = models.IntegerField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' by ' + self.author

from django.contrib.auth.models import User
from django.utils.timezone import now
class Comments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(default=now)

    def __str__(self):
        return self.post
