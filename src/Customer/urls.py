from django.conf.urls import patterns, url

from .views import register,signin,logoutAccount,editAccount,change_password

urlpatterns=patterns('',
    url(r'^$',register,name='register'),
    url(r'^signin/$',signin,name="signin"),
    url(r'^edit/$',editAccount,name='edit'),
    url(r'^logout/$',logoutAccount,name="logout"),
    url(r'^change_password/$', change_password,name="change_password"),
    )
