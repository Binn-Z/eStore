from django.db import models

# Create your models here.
class Customer(models.Model):
	c_Name=models.CharField(max_length=20,verbose_name='姓名')
	c_Phone=models.CharField(max_length=20,unique=True,verbose_name='手机号码')
	c_Password=models.CharField(max_length=20,verbose_name='密码')
	c_Address=models.CharField(max_length=100,verbose_name='地址')
	c_Cost=models.DecimalField(max_digits=12,default=0.00,decimal_places=2,verbose_name='历史消费')
	m_Level=models.ForeignKey("Member",default=1,verbose_name='会员等级')
	

	def __str__(self):
		return self.c_Name

	class Meta:
		ordering=['c_Name']
		verbose_name = u'顾客'
		verbose_name_plural = u'顾客'

class Member(models.Model):
	m_Description=models.CharField(max_length=100,blank=True,verbose_name='等级描述')
	m_Discount=models.FloatField(verbose_name='优惠')
	m_Level=models.IntegerField(primary_key=True,verbose_name='会员等级')

	def __str__(self):
		return str(self.m_Level)

	class Meta:
		ordering=['m_Level']
		verbose_name = u'会员等级'
		verbose_name_plural = u'会员等级'