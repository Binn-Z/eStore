from django.db import models

# Create your models here.
class Orders(models.Model):
	c_Id=models.ForeignKey("Customer.Customer",verbose_name='顾客')
	o_Date=models.DateField(auto_now=True,verbose_name='订单日期')
	o_Status=models.BooleanField(verbose_name='订单状态')
	g_Id=models.ForeignKey("Goods.Goods",verbose_name='商品')
	o_Amount=models.IntegerField(verbose_name='商品数量')
	o_Address=models.CharField(max_length=100,verbose_name='配送地址')
	o_Description=models.CharField(max_length=100,blank=True,verbose_name='备注')
	o_Contact=models.CharField(max_length=20,verbose_name='联系方式')
	o_total=models.DecimalField(max_digits=8,decimal_places=2,verbose_name='订单总额')

	def __str__(self):
		return str(self.id)

	class Meta:
		ordering=['id']
		verbose_name = u'订单'
		verbose_name_plural = u'订单'