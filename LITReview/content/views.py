from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Ticket


@login_required
def flux(request):
	return render(request, "content/flux.html")


@login_required
def review(request):
	return render(request, "content/review.html")


@login_required
def follow(request):
	return render(request, "content/follow.html")


@login_required
def modify_review(request):
	return render(request, "content/modify_review.html")


@login_required
def modify_ticket(request):
	return render(request, "content/modify_ticket.html")


@login_required
def posts(request):
	return render(request, "content/posts.html")


@login_required
def ticket(request):
	tickets = Ticket.objects.all()

	context = {
		'tickets': tickets
	}
	return render(request, "content/ticket.html", context)
