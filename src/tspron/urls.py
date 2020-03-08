from django.conf.urls import url

from . import views

app_name = 'tspron'
urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'faq/', views.faq, name='faq'),
]
