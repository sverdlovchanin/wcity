from django.shortcuts import render
from random import randint
from .models import Fenster
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

def index(request):
	# test_creation()
	fenster_list = Fenster.objects.order_by("id")
	context = {
		"window_height": 100,
		"window_width": fenster_list[0].fenster_width,
		"fenstertypes": [True, False],
		"how_many_fenster": len(fenster_list),
		"request_place": str(request)
	}
	try:
		if 'selected_fenster' in request.POST:
			fenster_id = request.POST['selected_fenster']
			print(fenster_id)
			buy(request, fenster_id)
		#context['request_place'] += str(request.POST)
	except Exception as e:
		context["an exception"] = str(e) + str(type(e))
	return display_all(request, context)

def buy(request, fenster_id):
	f = Fenster.objects.get(pk=fenster_id)
	f.status_of_object = False
	f.save()
	if request.method == "POST":
		f = Fenster.objects.get(
			pk=request.POST['selected_fenster']
		)
		f.for_rent=False
		f.save()
		print("from: %s " % ('462243@e1.ru', ))
		send_mail(
			subject='Fenster was sold',
			message='Fenster #%i was sold.' % f.id,
			from_email='*@e1.ru',
			recipient_list=['*@mail.ru'],
			auth_user="*",
			auth_password=yapass,
			fail_silently=False,
		)
	return HttpResponseRedirect("/fenster")
	

@login_required
def sell(request):
# Sell a new Fenster.
	if request.method == "POST":
		f = Fenster(
			fenster_width=request.POST['fenster_width'],
			fenster_height=request.POST['fenster_height'],
			fenster_scheme=request.POST['fenster_scheme'],
			latitude=request.POST['latitude'],
			longitude=request.POST['longitude'],
			altitude=request.POST['altitude'],
			price=request.POST['price'],
			window_view=''
		)
		f.save()
		return render(request, 'fenster/success.html')
	else:
		return render(request, 'fenster/new.html')		

def display_all(request, context={}):
	fenster_list = Fenster.objects.order_by("id")
	context["fenster_list"] = fenster_list
	return render(request, 'fenster/index.html', context)

def test_creation():
# Create a new Fenster.
	f = Fenster(
		fenster_width=randint(100,256),
		fenster_height=randint(100,256),
		window_view=''
	)
	f.save()
