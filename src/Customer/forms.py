from django import forms
from .models import Customer

class ChangepasswordForm(forms.Form): 
    old_password = forms.CharField(label=(u"原密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,})) 
    new_password = forms.CharField(label=(u"新密码"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,})) 
    new_password1 = forms.CharField(label=(u"新密码确认"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,})) 

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['c_Name','c_Phone','c_Password','c_Address']
        widgets = {
                "c_Password": forms.PasswordInput
            }

class SigninForm(forms.Form):
	c_Phone=forms.CharField(widget = forms.TextInput,label='手机号码')
	c_Password=forms.CharField(widget =forms.PasswordInput,label='密码')

class UpdateForm(forms.Form):
	c_Name = forms.CharField(widget = forms.TextInput,label='姓名')
	c_Address = forms.CharField(widget = forms.TextInput,label='地址')

class ChangepasswordForm(forms.Form):
    oldpassword = forms.CharField(label="原密码",widget=forms.PasswordInput) 
    newpassword1 = forms.CharField(label="新密码",widget=forms.PasswordInput)
    newpassword2 = forms.CharField(label="确认密码",widget=forms.PasswordInput)
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"所有项都为必填项")
        elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        else:
            cleaned_data = super(ChangepasswordForm, self).clean()
        return cleaned_data

