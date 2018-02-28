# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# import datetime

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .forms import PersonForm, RentForm
from .models import Person, User, Rent, Car

from django.shortcuts import render

# def home(request):
# 	return render(request, 'home.html', {'key': "value" })

class CreatePersonView(CreateView):
	queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/admin'

# class UpdatePersonView(UpdateView):
# 	queryset = Person.objects.all()
# 	template_name='person.html'
# 	form_class = PersonForm
# 	success_url = '/'

class ListPersonView(ListView):
    model = Person
    template_name='person_list.html'

class CreateRentView(CreateView):
	# queryset = Rent(), Car()
	template_name='rent.html'
	form_class = RentForm
	success_url = 'myapp/templates/profile.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(CreateRentView, self).form_valid(form)

class ListCarView(ListView):
	model=Car
	template_name='Car.html'
