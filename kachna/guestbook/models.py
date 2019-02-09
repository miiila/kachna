from django.db import models

class Post(models.Model):

    text = models.TextField(max_length=2000)
    author_name = models.CharField(max_length=100)
    author_email = models.CharField(max_length=50)
    timestamp = models.DateTimeField('date published', auto_now=True)

    def __str__(self):
        return self.text

