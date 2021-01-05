from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateTimeField
from django.utils import timezone
from django.db import models

# Create your models here.

GOVERNS = ('AlSharkia',('AlSharkia')),('Alexandria',('Alexandria')),('Cairo',('Cairo'))

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(default=' ')
    govern = models.CharField(max_length=50,choices=GOVERNS)
    date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=CASCADE)

    def __str__(self):
        return self.title
        
    class Meta:
        ordering = ('-date',)

