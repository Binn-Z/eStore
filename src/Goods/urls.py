from django.conf.urls import patterns, url

from .views import Goods_ListView,Goods_DetailView,addCart
urlpatterns=patterns('',
    url(r'^(?P<method>\w+)/(?P<arg>\d+)/$',Goods_ListView.as_view(),name='index'),
    url(r'^(?P<id>\d+)/$',Goods_DetailView.as_view(),name='detail'),
    url(r'^(?P<id>\d+)/addCart/$',addCart,name='addCart'),
    )
