from django.conf.urls import patterns, url, include

from .views import Orders_ListView,Cart_ListView
urlpatterns=patterns('',
	url(r'^cart/$',Cart_ListView.as_view(),name='cart'),
    url(r'^orders/$',Orders_ListView.as_view(),name='orders'),
    )
