from django.conf.urls import  url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
     url(r'^api/v1/categories/$', views.category_collection, name='category_collection'),
]
