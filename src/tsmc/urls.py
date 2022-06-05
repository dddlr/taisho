from django.urls import path

from . import views

app_name = 'tsmc'
urlpatterns = [
    path('', views.search, name='search'),
    path('<int:pk>/', views.CharacterView.as_view(), name='character'),
]
