from django.forms import ModelForm
from .models import Orders,Packages,contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 	


class OrderForm(ModelForm):
	class Meta:
		model = Orders
		fields = '__all__'


class PackageForm(ModelForm):
	class Meta:

		model = Packages
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class SubmitContactForm(ModelForm):
	class Meta:
		model = contact
		fields = "__all__"
		