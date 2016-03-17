from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Goods(models.Model):
	g_Name=models.CharField(max_length=20,verbose_name='商品名称')
	g_Price=models.DecimalField(max_digits=6,decimal_places=2,verbose_name='商品售价')
	g_Description=models.TextField(verbose_name='商品描述')
	g_Cost=models.DecimalField(max_digits=6,decimal_places=2,verbose_name='商品成本')
	g_Picture=models.ImageField(upload_to='photos/',verbose_name='商品图片')
	g_Num=models.IntegerField(verbose_name='商品库存')
	g_ProductDate=models.DateField(verbose_name='生产日期')
	g_ExpirationTime=models.IntegerField(verbose_name='保质期(月)')
	g_Discount=models.FloatField(default=1.0,verbose_name='商品折扣')
	t_Id=models.ForeignKey("Goods_Type",verbose_name='商品类别')

	def __str__(self):
		return self.g_Name

	class Meta:
		ordering=['g_Name']
		verbose_name = u'商品'
		verbose_name_plural = u'商品'

class Goods_Type(models.Model):
	t_Name=models.CharField(max_length=20,unique=True,verbose_name='商品类别')
	t_Description=models.CharField(max_length=100,blank=True,verbose_name='类别描述')

	def __str__(self):
		return self.t_Name

	class Meta:
		ordering=['t_Name']
		verbose_name = u'商品类别'
		verbose_name_plural = u'商品类别'