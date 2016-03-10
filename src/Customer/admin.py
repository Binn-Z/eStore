from django.contrib import admin

from .models import Customer,Member
# Register your models here.
class Customer_Admin(admin.ModelAdmin):
	list_filter=['m_Level__m_Level']
	list_display=['c_Name','c_Phone','c_Address','m_Level','c_Cost']

	class Meta:
		model=Customer

class Member_Admin(admin.ModelAdmin):
	list_display=['m_Level','m_Discount','m_Description']
	list_filter=['m_Level']

	class Meta:
		model=Member

admin.site.register(Customer,Customer_Admin)
admin.site.register(Member,Member_Admin)