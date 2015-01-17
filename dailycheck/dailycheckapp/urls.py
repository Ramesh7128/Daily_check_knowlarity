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
    url(r'profile/employeelist/$', views.employee_list, name='employeelist'),
)
