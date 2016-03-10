from django import forms
from .models import Customer

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['c_Name','c_Phone','c_Password','c_Address']
