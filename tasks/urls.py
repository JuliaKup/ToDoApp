from django.conf.urls import url
from . import views

app_name = 'tasks'
urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/$', views.create, name='create'),
    url(r'^remove_task/$', views.remove_task, name='remove_task'),
]