from django.shortcuts import render
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView

from .models import Goods,Goods_Type
from Comment.models import Comment
# Create your views here.

class Goods_ListView(ListView):

	model=Goods
	template_name="GoodsList.html"
	paginate_by=9

	def get_context_data(self, **kwargs):
		context = super(Goods_ListView, self).get_context_data(**kwargs)
		context['goods_types'] = Goods_Type.objects.all()
		return context


class Goods_DetailView(DetailView):
	model=Goods
	template_name="GoodsDetail.html"
	pk_url_kwarg='id'

	def get_context_data(self, **kwargs):
		context = super(Goods_DetailView, self).get_context_data(**kwargs)
		context['comment_list']=Comment.objects.filter(g_Id__exact=kwargs['object'].id)
		return context

