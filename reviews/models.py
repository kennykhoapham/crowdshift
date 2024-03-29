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

class ProfilePhoto(models.Model):
	user = models.ForeignKey(User)
	photo = models.FileField(upload_to='profile-photos')

class ReviewPhoto(models.Model):
	review = models.ForeignKey(Review)
	photo = models.FileField(upload_to='review-photos')

class VehiclePhoto(models.Model):
	vehicle = models.ForeignKey(Vehicle)
	photo = models.FileField(upload_to='vehicle-photos')
#class ProfilePhoto(models.Model):