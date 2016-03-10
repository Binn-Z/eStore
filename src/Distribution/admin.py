from django.contrib import admin

from .models import Distribution,Deliveryman
# Register your models here.
class Distribution_Admin(admin.ModelAdmin):
	list_filter=['d_Date','p_Id__p_Name']
	list_display=['o_Id','p_Id','d_Date']

	class Meta:
		model=Distribution

class Deliveryman_Admin(admin.ModelAdmin):
	list_display=['p_Name','p_Sex','p_Phone','p_Num']

	class Meta:
		model=Deliveryman

admin.site.register(Distribution,Distribution_Admin)
admin.site.register(Deliveryman,Deliveryman_Admin)