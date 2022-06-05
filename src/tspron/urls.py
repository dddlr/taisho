from django.urls import path, re_path

from . import views

app_name = 'tspron'
urlpatterns = [
    path('', views.search, name='search'),
    re_path(r'about/', views.about, name='about'),
]
