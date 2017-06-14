from django.conf.urls import include, url
from django.contrib import admin
from Blog_app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'Blog_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.lists, name='list'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<id>\d+)/$', views.details, name='details'),
    url(r'^update/$', views.update, name='update'),
    url(r'^delete/$', views.delete, name='delete'),
 
]
