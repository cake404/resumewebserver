from django.urls import path

from . import views

app_name = 'projectsapp'
urlpatterns = [
    path('', views.index, name='index'),
]