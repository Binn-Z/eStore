from django.shortcuts import render
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.http import HttpResponse

from .models import Orders
from Customer.models import Customer
# Create your views here.

class Orders_ListView(ListView):

	model=Orders
	template_name="OrdersList.html"
	paginate_by=9

	def get_context_data(self, **kwargs):
		userid=self.request.user.id
		if  userid != None:
			c_Phone = User.objects.get(id=userid).username
			customer = Customer.objects.get(c_Phone=c_Phone)
			context = super(Orders_ListView, self).get_context_data(**kwargs)
			context['is_login'] = True
			context['object_list'] = Orders.objects.filter(o_Status__exact=1,c_Id__exact=customer.id)
		else:
			context = super(Orders_ListView, self).get_context_data(**kwargs)
			context['object_list'] = None
			context['is_login'] = False
		return context

class Cart_ListView(ListView):

	model=Orders
	template_name="CartList.html"
	paginate_by=9

	def get_context_data(self, **kwargs):
		userid=self.request.user.id
		if  userid != None:
			c_Phone = User.objects.get(id=userid).username
			customer = Customer.objects.get(c_Phone=c_Phone)
			context = super(Cart_ListView, self).get_context_data(**kwargs)
			context['is_login'] = True
			context['object_list'] = Orders.objects.filter(o_Status__exact=0,c_Id__exact=customer.id)
		else:
			context = super(Cart_ListView, self).get_context_data(**kwargs)
			context['object_list'] = None
			context['is_login'] = False
		return context