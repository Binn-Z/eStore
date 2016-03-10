from django.contrib import admin

from .models import Comment
# Register your models here.
class Comment_Admin(admin.ModelAdmin):
	list_filter=['g_Id__g_Name','c_Id__c_Name','c_Date']
	list_display=['c_Id','g_Id','c_Date','c_Content']

	class Meta:
		model=Comment

admin.site.register(Comment,Comment_Admin)
