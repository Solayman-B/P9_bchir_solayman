from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from LITReview import forms
from LITReview.forms import authentification_form


def index(request):
	login_form = forms.authentification_form()
	if request.method == 'POST':
		login_form = forms.authentification_form(request.POST)
		if login_form.is_valid():
			user = authenticate(
				username=login_form.cleaned_data['username'],
				password=login_form.cleaned_data['password1'],
			)
			if user is not None:
				login(request, user)
				return redirect('/content/flux')
			else:
				messages.info(request, 'Identifiant et/ou mot de passe invalide(s)')
	return render(
		request, 'members/index.html', context={'form': login_form}
	)

def inscription(request):
	inscription_form = authentification_form(request.POST)
	context = {'form':inscription_form}
	return render(request, "members/inscription.html", context)