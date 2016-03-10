from django.db import models

# Create your models here.
class Comment(models.Model):
	c_Id=models.ForeignKey('Customer.Customer',verbose_name='顾客')
	g_Id=models.ForeignKey('Goods.Goods',verbose_name='商品')
	c_Date=models.DateField(verbose_name='评论日期')
	c_Content=models.TextField(verbose_name='评论内容')

	def __str__(self):
		return str(self.id)

	class Meta:
		ordering=['-c_Date']
		verbose_name = u'评论'
		verbose_name_plural = u'评论'
