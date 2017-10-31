from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
               url(r'^student/(?P<s_id>[0-9]+)/$', views.s_detail, name='s_detail'),
               url(r'^student/(?P<s_id>[0-9]+)/tutor/(?P<t_id>[0-9]+)/$', views.t_detail, name='t_detail'),
               url(r'^student/(?P<s_id>[0-9]+)/list/$', views.t_list, name='t_list'),
               url(r'^student/(?P<s_id>[0-9]+)/list/rate/$', views.t_sort, name='t_sort'),
               url(r'^student/(?P<s_id>[0-9]+)/list/search/$', views.t_search, name='t_search'),
               ]