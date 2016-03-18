from django.shortcuts import render
from  django.views.generic.list import ListView
from  django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Goods,Goods_Type
from Customer.models import Customer
from Comment.models import Comment
from Orders.models import Orders
from urllib.parse import unquote
import re
# Create your views here.

def addCart(request,**kwargs):
	if request.method=='POST':
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
		if self.request.META.get('HTTP_REFERER')==None or re.match(r".*?key=(.*)", self.request.META.get('HTTP_REFERER'))==None :  #last_key:前一次操作中搜索的额关键字
			last_key=''
		else:
			last_key=unquote(re.match(r".*?key=(.*)",self.request.META.get('HTTP_REFERER')).group(1))
		key=self.request.GET.get('key',last_key)
		if self.kwargs.get('filter')==None or self.kwargs.get('filter')=='0':
			queryset=Goods.objects.filter(g_Name__contains=key)
		else :
			queryset=Goods.objects.filter(t_Id__exact=self.kwargs.get('filter'),g_Name__contains=key)
		if self.kwargs.get('sort')=='3':    #折扣最多
			return queryset.order_by('g_Discount')
		elif self.kwargs.get('sort')=='1':  #价格升序
			return queryset.order_by('g_Price')
		elif self.kwargs.get('sort')=='2':  #价格降序
			return queryset.order_by('-g_Price')
		else:								#默认排序
			return queryset

	def get_context_data(self, **kwargs):
		context = super(Goods_ListView, self).get_context_data(**kwargs)
		context['goods_types'] = Goods_Type.objects.all()
		context['sort_now']= 0 if re.match(r'/\w+/(\d+)/\d+', self.request.path)==None else re.match(r'/\w+/(\d+)/\d+', self.request.path).group(1) 
		context['filter_now']=0 if re.match(r'/\w+/\d+/(\d+)', self.request.path)==None else re.match(r'/\w+/\d+/(\d+)', self.request.path).group(1) 
		return context

	

class Goods_DetailView(DetailView):
	model=Goods
	template_name="GoodsDetail.html"
	pk_url_kwarg='id'

	def get_context_data(self, **kwargs):
		userid=self.request.user.id
		context = super(Goods_DetailView, self).get_context_data(**kwargs)
		context['comment_list']=Comment.objects.filter(g_Id__exact=kwargs['object'].id)
		if  userid != None:
			c_Phone = User.objects.get(id=userid).username
			customer = Customer.objects.get(c_Phone=c_Phone)
			context['is_login'] = True
		else:
			context['is_login'] = False

		return context

#添加评论
def addComment(request,**kwargs):
	if request.method=='POST':
		userid=request.user.id
		if  userid != None:   			#获取当前登录用户
			c_Phone = User.objects.get(id=userid).username
			customer = Customer.objects.get(c_Phone=c_Phone)
			comment=Comment(c_Id=customer,g_Id=Goods.objects.get(id=request.POST['Goods_id']),c_Content=request.POST.get('comment'))
			comment.save()
			return HttpResponse('添加成功')
	
	return HttpResponse('添加失败')