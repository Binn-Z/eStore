from django.db import models

# Create your models here.
class Customer(models.Model):
	c_Name=models.CharField(max_length=20)
	c_Phone=models.CharField(max_length=20,unique=True)
	c_Address=models.CharField(max_length=100)
	c_Cost=models.DecimalField(max_digits=12,decimal_places=2)
	m_Level=models.ForeignKey("Member")
	c_Password=models.CharField(max_length=20)

	def __str__(self):
		return self.c_Name


class Member(models.Model):
	m_Description=models.CharField(max_length=100,blank=True)
	m_Discount=models.FloatField()
	m_Level=models.IntegerField()

	def __str__(self):
		return self.m_Level