from django.db import models
from django.core.validators import int_list_validator

# Create your models here.

class Fenster(models.Model):
	fenster_width = models.IntegerField(default=50)
	fenster_height = models.IntegerField(default=50)
	fenster_scheme = models.CharField(
		validators=[int_list_validator],
		default='1,2',
		max_length=1024
	)

	window_view = models.CharField(
		default='',
		max_length=1024
	)

	latitude = models.FloatField(null=False)
	longitude = models.FloatField(null=False)
	altitude = models.FloatField(null=False)
	price = models.FloatField(null=False)
	status_of_object = models.BooleanField(default=1)
