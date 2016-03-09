from django.db import models

# Create your models here.
class Orders(models.Model):
	c_Id=models.ForeignKey("Customer.Customer")
	o_Date=models.DateField(auto_now=True)
	o_Status=models.BooleanField()
	g_Id=models.ForeignKey("Goods.Goods")
	o_Amount=models.IntegerField()
	o_Address=models.CharField(max_length=100)
	o_Description=models.CharField(max_length=100,blank=True)
	o_Contact=models.CharField(max_length=20)
	o_total=models.DecimalField(max_digits=8,decimal_places=2)

	def __str__(self):
		return self.id