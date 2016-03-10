from django.db import models

# Create your models here.
class Distribution(models.Model):
	o_Id=models.ForeignKey("Orders.Orders",verbose_name='订单编号')
	p_Id=models.ForeignKey("Deliveryman",verbose_name='配送员')
	d_Date=models.DateField(auto_now=True,verbose_name='配送单日期')

	def __str__(self):
		return str(self.id)

	class Meta:
		ordering=['id']
		verbose_name = u'配送单'
		verbose_name_plural = u'配送单'



class Deliveryman(models.Model):
	SEX_CHOICES=(
		(0,'女'),
		(1,'男'),
		)
	p_Name=models.CharField(max_length=20,verbose_name='配送员姓名')
	p_Sex=models.IntegerField(choices=SEX_CHOICES,verbose_name='性别')
	p_Phone=models.CharField(max_length=20,verbose_name='手机号码')
	p_Num=models.IntegerField(verbose_name='配送量')

	def __str__(self):
		return self.p_Name

	class Meta:
		ordering=['p_Name']
		verbose_name = u'配送员'
		verbose_name_plural = u'配送员'