from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vehicle(models.Model):
	make = models.CharField(max_length=30)
	model = models.CharField(max_length=30)
	year = models.IntegerField()

	def __unicode__(self):
		return str(self.year) + ' ' + self.make + ' ' + self.model


class Review(models.Model):
	title = models.CharField(max_length=60)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	vehicle = models.ForeignKey(Vehicle)
	author = models.ForeignKey(User)
	def __unicode__(self):
		return str(self.title) +  ' by ' + str(self.author)
