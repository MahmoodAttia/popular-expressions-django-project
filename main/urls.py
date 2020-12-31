from django.urls import path,include
from . import views
from .views import SearchResultsView
urlpatterns = [
    path('',views.home,name='home'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]