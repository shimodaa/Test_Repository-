from django.urls import path
from . import views


app_name = 'template_app'
urlspatterns = [
    path(' ', views.index, name='index'),
    path('home', views.home, name='home'),
    path('sample1', views.sample1, name='sample1'),
    path('sample2', views.sample2, name='sample2'),
]
