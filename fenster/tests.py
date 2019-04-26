from django.test import TestCase
from django.test import Client
from django.http import HttpResponse
from .models import Fenster

# Create your tests here.

class FensterTest(TestCase):
	def setUp(self):
		self.client=Client()
		f = Fenster(
			fenster_width = 10,
			fenster_height = 10,
			fenster_scheme = 1,
			latitude = 60.25,
			longitude = 55.25,
			altitude = 350,
			price = 300,
			window_view='',
		)

	def test_buy(self):
		response = self.client.post(
			'fenster/buy/',
			{
				'selected_fenster':128
			}
		)
		self.assertIsInstance(
			response,
			HttpResponse
		)

	def test_index(self):
		2/0
