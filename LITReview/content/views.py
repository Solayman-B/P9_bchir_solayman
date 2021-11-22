from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket
from .forms import TicketForm


@login_required
def flux(request):
	tickets = Ticket.objects.order_by('-id').all()
	#tickets = Ticket.objects.filter(id = request.user.id)

	context = {
		'tickets': tickets
	}
	return render(request, "content/flux.html", context)


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
	if request.method == 'POST':
		form = TicketForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('content:flux')
	else:
		form = TicketForm()

	context = {
		'form': form,
	}
	return render(request, "content/ticket.html", context)
