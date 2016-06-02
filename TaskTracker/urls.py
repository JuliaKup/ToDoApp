"""TaskTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from TaskTracker import views
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^$', views.index, name='index'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/', views.RegisterView.as_view(model=User, get_success_url = lambda: reverse('tasks'), form_class=UserCreationForm, template_name="registration/register.html"), name='register'),
    url(r'^create_project/', views.create_project, name='create_project'),
    url(r'^(?P<pk>[0-9]+)/$', views.project, name='project'),
]
