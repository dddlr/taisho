from django.conf.urls import url

from . import views

app_name = 'tsmc'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.CharacterView.as_view(), name='character'),
    url(r'^search/$', views.search, name='search'),
]
