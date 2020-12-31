from django.db.models.fields import DateTimeField
from django.utils import timezone
from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default=' ')
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('-date',)

