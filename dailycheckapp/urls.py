from django.conf.urls import patterns, include, url
from django.contrib import admin
from dailycheckapp import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dailycheck.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^user/', include('oautherise.urls')),
    url(r'^addEmployees/', views.addEmployees, name='addEmployees'),
    url(r'^profile/employlist/$', views.employlist, name='employlist'),
    url(r'^prof/(?P<userid>\w+)/$', views.emplprofile, name='profile'),
    url(r'^logpost/$', views.emplpost, name='emlpost'),
)
