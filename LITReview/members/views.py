from django.shortcuts import render

def index (request):
	return render(request, "members/index.html")

def inscription(request):
	return render(request, "members/inscription.html")