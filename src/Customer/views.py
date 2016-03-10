from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .forms import RegisterForm
# Create your views here.
def test(request):
	if request.method == 'POST': # 如果表单被提交
		form = RegisterForm(request.POST) # 获取Post表单数据
		if form.is_valid(): # 验证表单
			return HttpResponseRedirect('/') # 跳转
	else:
		form = RegisterForm() #获得表单对象
	return render(request,'register.html',{'form': form})

	