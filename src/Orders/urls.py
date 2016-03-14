from django.conf.urls import patterns, url, include

from .views import Orders_ListView
urlpatterns=patterns('',
    url(r'^cart/$',Orders_ListView.as_view(),name='cart')
    )
