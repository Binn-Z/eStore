from django.contrib import admin

from .models import Goods,Goods_Type
# Register your models here.
class Goods_Admin(admin.ModelAdmin):
	list_display=['g_Name','g_Price','g_Cost','g_Num','g_Discount','t_Id']
	list_filter=['t_Id__t_Name','g_Num','g_ProductDate']
	class Meta:
		model=Goods

class Goods_Type_Admin(admin.ModelAdmin):
	list_display=['t_Name','t_Description']

	class Meta:
		model=Goods_Type

admin.site.register(Goods,Goods_Admin)
admin.site.register(Goods_Type,Goods_Type_Admin)