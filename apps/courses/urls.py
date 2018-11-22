from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name="index"),
    url(r'^courses/create/$', views.create,name="create"),
    url(r'^courses/delete/(?P<id>\d+)$', views.delete,name="my_delete"),
     url(r'^courses/destroy/(?P<id>\d+)$', views.confirm,name="my_confirm"),
   
]
