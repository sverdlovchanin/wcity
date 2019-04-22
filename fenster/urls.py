from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('', views.index, name='buy'),
	path('sell/', views.sell, name='sell'),
]
