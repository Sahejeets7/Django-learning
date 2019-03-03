from django.db import models

# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published = models.DateTimeField('date published')

    def __str__(self):
        return self.title
