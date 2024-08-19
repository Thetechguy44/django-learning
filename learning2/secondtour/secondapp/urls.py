from django.urls import path
from . import views

# define our urls
urlpatterns = [
    path('', views.index)
]