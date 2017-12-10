from django.conf.urls import url

from . import views

app_name = 'tsmc'
urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^(?P<pk>[0-9]+)/$', views.CharacterView.as_view(), name='character'),
]
