from django.db import models

# Create your models here.

class Post(models.Model):
    postID = models.AutoField(primary_key=True)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    content = models.TextField()
    slug = models.CharField(max_length=500)
    date = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author