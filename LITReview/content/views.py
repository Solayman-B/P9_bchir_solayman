from django.shortcuts import render

def flux(request):
	return render(request, "content/flux.html")