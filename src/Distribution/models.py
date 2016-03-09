from django.db import models

# Create your models here.
class Distribution(models.Model):
	o_Id=models.ForeignKey("Orders.Orders")
	p_Id=models.ForeignKey("Deliveryman")
	d_Date=models.DateField(auto_now=True)

	def __str__(self):
		return self.id



class Deliveryman(models.Model):
	p_Name=models.CharField(max_length=20)
	p_Sex=models.BooleanField()
	p_Phone=models.CharField(max_length=20)
	p_Num=models.IntegerField()

	def __str__(self):
		return self.p_Name