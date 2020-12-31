from django.urls import path,include
from . import views
from .views import SearchResultsView, creatpost
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('',views.home,name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('register/', views.register, name='register'),
    path('add/', creatpost.as_view(), name='add'),
    path('update/<str:pk>' ,views.update, name="update"),
    path('delete/<str:pk>' ,views.delete, name="delete"),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='index.html'),name='logout'),
    path('profile',views.profile,name='profile'),
]

