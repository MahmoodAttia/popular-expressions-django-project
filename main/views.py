from django.db.models.query_utils import Q
from main.models import Post
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def home(request):
    return render(request,template_name="index.html")

class SearchResultsView(ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list