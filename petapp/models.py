from django.db import models

# Create your models here.

class Pet(models.Model):
	name = models.CharField(max_length=50)
	age = models.IntegerField()
	available = models.BooleanField(default=True)
	image = models.ImageField(null=True, blank=True)
	price = models.DecimalField(max_digits=7, decimal_places=3)

	def __str__(self):
		return self.name