from django.conf.urls import patterns, url, include

from .views import test

urlpatterns=patterns('',
    url(r'^$',test),
    )
