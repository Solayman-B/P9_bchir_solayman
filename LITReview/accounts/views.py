from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.forms import UserForm


def login(request):
	login_form = UserForm()
	if request.method == 'POST':
		login_form = UserForm(request.POST)
		if login_form.is_valid():
			print('coucou3')
			user = authenticate(
				username=login_form.cleaned_data['username'],
				password=login_form.cleaned_data['password'],
			)
			if user is not None:
				auth_login(request, user)
				return redirect('content/')
			else:
				messages.info(request, 'Identifiant et/ou mot de passe invalide(s)')
	print('pas coucou')
	return render(
		request, 'accounts/login.html', context={'form': login_form}
	)



def register(response):
	if response.method == "POST":
		register_form = UserForm(response.POST)
		if register_form.is_valid():
			register_form.save()
		return redirect("/")
	else:
		register_form = UserForm()
	return render(response, "accounts/register.html", {'form': register_form})
