from django.shortcuts import render
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Goods,Goods_Type
from Customer.models import Customer
from Comment.models import Comment
from Orders.models import Orders
# Create your views here.

def addCart(request,**kwargs):
	if request.method=='POST':
		print(request.POST)
		userid=request.user.id
		if  userid != None:   			#获取当前登录用户
			c_Phone = User.objects.get(id=userid).username
			customer = Customer.objects.get(c_Phone=c_Phone)
			cartOrder=Orders(c_Id=customer,g_Id=Goods.objects.get(id=request.POST['Goods_id']),
							o_Amount=request.POST['Goods_num'],o_Status=0,
							o_Address=customer.c_Address,o_Contact=customer.c_Phone,
							o_total=float(request.POST['Goods_num'])*float(request.POST['Goods_price'])*float(request.POST['Goods_discount']))
			cartOrder.save()
			return HttpResponse('添加成功')
	
	return HttpResponse('添加失败')

class Goods_ListView(ListView):
	model=Goods
	template_name="GoodsList.html"
	paginate_by=9

	def get_queryset(self):
		if self.kwargs.get('method')=='Sort':
			print(type(self.kwargs.get('arg')))
			if self.kwargs.get('arg')=='0':    #默认排序
				return Goods.objects.all()
			elif self.kwargs.get('arg')=='1':  #价格升序
				return Goods.objects.all().order_by('g_Price')
			elif self.kwargs.get('arg')=='2':  #价格降序
				return Goods.objects.all().order_by('-g_Price')
			else:								#折扣最多
				return Goods.objects.all().order_by('g_Discount')
		else:
			# return Goods.objects.filter(g_Id__exact=self.kwargs.get('arg'))
			return Goods.objects.filter(t_Id__exact=self.kwargs.get('arg'))

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

