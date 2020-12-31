from django.views.generic.edit import CreateView
from main.forms import Addpost, reg
from django.db.models.query_utils import Q
from main.models import Post
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request,template_name="index.html")

class SearchResultsView(ListView):
    model = Post
    template_name = 'index.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),active=True
        )
        return object_list

def register(request):
    if request.method == 'POST':
        form = reg(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(form.cleaned_data['password1'])
            f.save()
    else:
        form = reg()
    return render(request,'reg.html',{'form':form})

class creatpost(LoginRequiredMixin,CreateView):
    model = Post
    fields = [
        'title','content'
    ]
    template_name='add.html'
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        


def update(request,pk): 
    order = Post.objects.get(id=pk)
    form = Addpost(instance=order) 
    if request.method == 'POST': 
       form = Addpost(request.POST, instance=order)
       if form.is_valid():
           form.save()
         
           return redirect('/')

    context = {'form':form}

    return render(request , 'add.html', context )


def delete(request,pk): 
    order = Post.objects.get(id=pk) 
    if request.method == 'POST':  
        order.delete()
        return redirect('/')

    context = {'order':order}

    return render(request , 'delete.html', context )

def profile(request):
    post = Post.objects.filter(user=request.user)
    return render(request,'profile.html',{'post':post})