from django.db import models

# Create your models here.
class Comment(models.Model):
	c_Id=models.ForeignKey('Customer.Customer')
	g_Id=models.ForeignKey('Goods.Goods')
	c_Date=models.DateField()
	c_Content=models.TextField()

	def __str__(self):
		return self.id