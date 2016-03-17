"""eStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Goods.views import Goods_ListView
urlpatterns = [
    url(r'^$',Goods_ListView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^Customer/',include('Customer.urls',namespace="Customer")),
    # url(r'^Comment/',include('Comment.urls')),
    # url(r'^Distribution/',include('Disatribution.urls')),
    url(r'^Goods/',include('Goods.urls',namespace="Goods")),
    url(r'^Orders/',include('Orders.urls',namespace="Orders")),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)