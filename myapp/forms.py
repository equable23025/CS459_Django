from django import forms
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import datetime
from .models import Person, Rent, Car

class PersonForm(ModelForm):
	class Meta:
		model =  Person
		exclude=[]

		# widgets = {
		# 	'dob': forms.DateInput(
		# 		attrs={
		# 		'type': 'date',
		# 		'value': datetime.datetime.now().strftime("%Y-%m-%d")
		# 		}, format="%Y-%m-%d"
		# 	),
		# }

	def __init__(self, *args, **kwargs):
		super(PersonForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))

class RentForm(ModelForm):
	class Meta:
		model = Rent
		exclude = ['user','price','stop']

	def __init__(self, *arg, **kwargs):
		super(RentForm, self).__init__(*arg, **kwargs)
		self.helper = FormHelper()
		self.helper.add_input(Submit('submit', 'Submit'))
