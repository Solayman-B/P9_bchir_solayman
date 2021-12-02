from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket, Review
from .forms import TicketForm, ReviewForm


@login_required
def flux(request):
	tickets = Ticket.objects.order_by('-id').filter(user_id=request.user.id)

	context = {
		'tickets': tickets
	}
	return render(request, "content/flux.html", context)


@login_required
def review(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			#si on clique sur créer une critique d'un ticket, rechercher instance du ticket l'attribuer à la critique
			review = Review.objects.create(user_id= request.user.pk, headline= request.POST.get('headline'), body= request.POST.get('body'))

			#si le ticket n'existe pas
			#review = Review(user_id= request.user.pk, headline= request.POST.get('headline'), body= request.POST.get('body'))
			#review.save()
			return redirect('content:flux')
	else:
		form = ReviewForm()

	context = {
		'form': form,
	}

	return render(request, "content/review.html", context)


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
			ticket = Ticket(user_id= request.user.pk, title= request.POST.get('title'), description= request.POST.get('description'))
			ticket.save()
			return redirect('content:flux')
	else:
		form = TicketForm()

	context = {
		'form': form,
	}
	return render(request, "content/ticket.html", context)
