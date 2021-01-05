import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet): 
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['govern']
       # exclude = ['book' , 'status']