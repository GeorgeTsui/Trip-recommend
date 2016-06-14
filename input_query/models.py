from django.db import models

# Create your models here.

class Comment(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()
	
	def __str__(self):
		return self.name

class Hotel(models.Model):
	hotel_id = models.CharField(max_length=500)
	name = models.CharField(max_length=100)
	rating = models.CharField(max_length=100)
	comment = models.CharField(max_length=100000)
	state = models.CharField(max_length=100)

	def __str__(self):
		return self.hotel_id
