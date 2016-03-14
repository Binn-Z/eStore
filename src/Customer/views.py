from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate,views
from django.core.urlresolvers import reverse

from .forms import RegisterForm,UpdateForm,SigninForm,ChangepasswordForm
from .models import Customer
# Create your views here.

#注册账号
def register(request):
	if request.method == 'POST': # 如果表单被提交
		form = RegisterForm(request.POST) # 获取Post表单数据
		if form.is_valid(): # 验证表单
			instance=form.save()
			user=User.objects.create_user(username=instance.c_Phone, password=instance.c_Password,email=instance.c_Phone) #创建user
			user=authenticate(username=instance.c_Phone, password=instance.c_Password)
			login(request,user)
			return HttpResponseRedirect('/Customer')
	else:
		form = RegisterForm() 
	return render(request,'register.html',{'form': form})


#登录账号
def signin(request):
	if request.method == 'POST': # 如果表单被提交
		form = SigninForm(request.POST) # 获取Post表单数据
		if form.is_valid(): # 验证表单
			user=authenticate(username=form.cleaned_data['c_Phone'], password=form.cleaned_data['c_Password'])
			if user is not None: #登陆成功
				login(request,user)
			else:
				return render(request,'signin.html',{'form': SigninForm(),"success_or_first":False})
			return HttpResponseRedirect(reverse("Goods:index")) #回到主页
	else:
		form = SigninForm() 
	return render(request,'signin.html',{'form': form,"success_or_first":True})

#登出账号
def logoutAccount(request):
	title = '退出成功'
	context = {
		"title": title,
	}
	logout(request)
	return render(request, "logout.html", context)


#修改账号信息
def editAccount(request):
	userId = request.user.id
	query = User.objects.get(id=userId)   #获取登录user
	c_Phone = query.email
	obj = Customer.objects.get(c_Phone=c_Phone)
	updateform = UpdateForm(request.POST or None, initial={'c_Name': obj.c_Name, 'c_Address': obj.c_Address})
	context = {
		"userId": userId,
		"updateform": updateform,
		"c_Cost": obj.c_Cost,
		"m_Level":obj.m_Level,
	}

	if 'deleteaccount' in request.POST:   #删除账号
		query.delete()
		obj.delete()
		return HttpResponseRedirect('/Customer') #回到主页

	if 'updateaccount' in request.POST:   #提交更新
		if updateform.is_valid():
			cd = updateform.cleaned_data
			Customer.objects.filter(c_Phone=c_Phone).update(c_Name=cd.get('c_Name'), c_Address=cd.get('c_Address'), c_Password=cd.get('c_Password'))
			query.delete()			
	return render(request, "editAccount.html", context)

#修改密码 changepassword_status：0(初始表单) -1(修改密码失败)  1(修改密码成功)
def change_password(request):
    if request.method == 'GET':
        form = ChangepasswordForm()
        return render(request,'changepassword.html',{'form': form,'changepassword_status':0})
    else:
        form = ChangepasswordForm(request.POST)
        if form.is_valid():
            c_Phone = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = authenticate(username=c_Phone, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                Customer.objects.filter(c_Phone=c_Phone).update(c_Password=newpassword)
                return render(request,'changepassword.html',{'changepassword_status':1})
            else:
                return render(request,'changepassword.html',{'changepassword_status':-1,'form':ChangepasswordForm()})
        else:
            return render(request,'changepassword.html',{'changepassword_status':-1,'form':ChangepasswordForm()})