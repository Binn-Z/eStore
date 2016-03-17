from django.conf.urls import patterns, url, include

from .views import Orders_ListView,Cart_ListView,Orders_DetailView,deleteCart,payCart
urlpatterns=patterns('',
	url(r'^cart/$',Cart_ListView.as_view(),name='cart'),
	url(r'^cart/delete/$',deleteCart,name='delete'),
	url(r'^cart/pay/$',payCart,name='pay'),
    url(r'^list/$',Orders_ListView.as_view(),name='list'),
    url(r'^(?P<id>\d+)/$',Orders_DetailView.as_view(),name='detail'),
    )
