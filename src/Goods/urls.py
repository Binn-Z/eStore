from django.conf.urls import patterns, url

from .views import Goods_ListView,Goods_DetailView
urlpatterns=patterns('',
    url(r'^$',Goods_ListView.as_view(),name='index'),
    url(r'^(?P<id>\d+)/$',Goods_DetailView.as_view(),name='detail'),
    )
