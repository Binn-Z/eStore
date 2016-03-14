from django.shortcuts import render
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView

from .models import Orders
# Create your views here.

class Orders_ListView(ListView):

	model=Orders
	template_name="OrdersList.html"
	paginate_by=9

	def get_context_data(self, **kwargs):
		context = super(Orders_ListView, self).get_context_data(**kwargs)
		context['object_list'] = Orders.objects.filter(o_Status__exact=1)
		return context