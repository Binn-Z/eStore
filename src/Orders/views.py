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
	paginate_by=10

	def get_queryset(self):
		userid=self.request.user.id
		if  userid != None:
			c_Phone = User.objects.get(id=userid).username
			customer = Customer.objects.get(c_Phone=c_Phone)
			return Orders.objects.filter(o_Status__exact=1,c_Id__exact=customer.id)
		else:
			return None

	def get_context_data(self, **kwargs):
		userid=self.request.user.id
		if  userid != None:
			c_Phone = User.objects.get(id=userid).username
			customer = Customer.objects.get(c_Phone=c_Phone)
			context = super(Orders_ListView, self).get_context_data(**kwargs)
			context['is_login'] = True
		else:
			context = super(Orders_ListView, self).get_context_data(**kwargs)
			context['is_login'] = False
		return context

class Orders_DetailView(DetailView):
	model=Orders
	template_name="OrdersDetail.html"
	pk_url_kwarg='id'

	def get_context_data(self, **kwargs):
		context = super(Orders_DetailView, self).get_context_data(**kwargs)
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
			context['customer']=customer
			context['object_list'] = Orders.objects.filter(o_Status__exact=0,c_Id__exact=customer.id)
		else:
			context = super(Cart_ListView, self).get_context_data(**kwargs)
			context['object_list'] = None
			context['is_login'] = False
		return context


def deleteCart(request):
	cart=Orders.objects.get(id=request.POST.get('id'))
	cart.delete()
	return HttpResponse('ok')

def payCart(request):
	print(request.POST)
	order=Orders.objects.get(id=request.POST.get('id'))
	order.o_Amount=request.POST.get('amount')
	order.o_Address=request.POST.get('address')
	order.o_Description=request.POST.get('description')
	order.o_Contact=request.POST.get('contact')
	order.o_Status=1
	order.save()
	return HttpResponse('ok')
