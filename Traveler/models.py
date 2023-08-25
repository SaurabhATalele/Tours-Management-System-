from django.db import models

class Packages(models.Model):
	CATEGORY = (
			('Group','Group'),
			('Solo','Solo'),
			('Trekking','Trekking')
		)

	pack_name = models.CharField(max_length=200,null=True)
	tripduration = models.CharField(max_length=200,null=True)
	destination = models.CharField(max_length=1000,null=True)
	price = models.FloatField(null=True)
	image = models.ImageField(upload_to='pics')
	date_created = models.DateTimeField(auto_now_add= True,null=True)
	category = models.CharField(max_length=200,null=True,choices = CATEGORY)

	description = models.TextField(max_length=2000, null=True)

	def __str__(self):
    		return self.pack_name



	

class Orders(models.Model):
    order_id = models.IntegerField()
    username = models.CharField(max_length=100)
    people = models.IntegerField()
    order_date = models.DateField()
    cost = models.IntegerField()
    pack_name = models.CharField(max_length=200)
    trip_date = models.DateField()
    

    def __str__(self):
        return self.order_id

  
class contact(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	number = models.CharField(max_length=10)
	subject = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class offers(models.Model):
	orders = models.IntegerField()
	offer = models.IntegerField()

	def __str__(self):
		return self.orders



