from django.db import models

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)

class Product(models.Model):
	pid = models.CharField(max_length=20)
	pname = models.CharField(max_length=100)
	pprice = models.IntegerField()
	class Meta:
		db_table = "products"

class Payment(models.Model):
	customer_id = models.CharField(max_length=20)
	amount = models.IntegerField()

	class Meta:
		db_table = "payments"