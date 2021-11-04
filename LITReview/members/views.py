from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from members.forms import UserForm


def login(request):
	login_form = UserForm()
	if request.method == 'POST':
		login_form = UserForm(request.POST)
		if login_form.is_valid():
			user = authenticate(
				username=login_form.cleaned_data['username'],
				password1=login_form.cleaned_data['password1'],
			)
			if user is not None:
				login(request, user)
				return redirect('')
			else:
				messages.info(request, 'Identifiant et/ou mot de passe invalide(s)')
	return render(
		request, 'members/login.html', context={'form': login_form}
	)

def register(request):
	register_form = UserForm(request.POST)
	context = {'form':register_form}
	return render(request, "members/register.html", context)