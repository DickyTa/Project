from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
               url(r'^student/(?P<s_id>[0-9]+)$', views.s_detail, name='s_detail'),
               url(r'^tutor/(?P<t_id>[0-9]+)$', views.t_detail, name='t_detail'),
               url(r'^list/$', views.t_list, name='t_list'),
               url(r'^list/rate/$', views.t_sort, name='t_sort'),
               url(r'^list/(?P<search>[^ \r\t\n\f]+)/$', views.t_search, name='t_search'),
               ]