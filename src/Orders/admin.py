from django.contrib import admin

from .models import Orders
# Register your models here.
class Orders_Admin(admin.ModelAdmin):
	list_display=['c_Id','g_Id','o_Date','o_total','o_Address','o_Description','o_Contact','o_Status']
	list_filter=['o_Date','o_total','c_Id__c_Name','g_Id__g_Name']

	class Meta:
		model=Orders


admin.site.register(Orders,Orders_Admin)