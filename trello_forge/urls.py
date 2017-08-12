"""trello_forge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as sign_in_view
from kanban import views
from kanban.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('kanban.urls')),
    url(r'^login/$', sign_in_view.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', sign_in_view.logout, {'next_page': '/login'}),
    url(r'^signup/$', views.signup, name='signup'),
]
