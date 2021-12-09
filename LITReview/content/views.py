from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.admin import User
from .models import Ticket, Review
from .forms import TicketForm, ReviewForm, UserFollowsForm, TicketDetailForm

@login_required
def ticket(request):
	if request.method == 'POST':
		form = TicketForm(request.POST)
		if form.is_valid():
			ticket = Ticket(user_id=request.user.pk, title=request.POST.get('title'),
							description=request.POST.get('description'))
			ticket.save()
			return redirect('content:flux')
	else:
		form = TicketForm()

	context = {'form': form}

	return render(request, "content/ticket.html", context)

@login_required
def ticket_detail(request, ticket_id):
	ticket = Ticket.objects.get(id=ticket_id)


	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = Review.objects.create(user_id=request.user.pk,
										   headline=request.POST.get('headline'),
										   rating=form.cleaned_data.get('rating'),
										   body=request.POST.get('body'))
			return redirect('content:flux')
	else:
		form = ReviewForm()

	context = {
		'ticket': ticket,
		'form': form
	}

	return render(request, "content/ticket_detail.html", context)

@login_required
def review(request):
	if request.method == 'POST':
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = Review.objects.create(user_id=request.user.pk,
										   headline=request.POST.get('headline'),
										   rating=form.cleaned_data.get('rating'),
										   body=request.POST.get('body'))
			return redirect('content:flux')
	else:
		form = ReviewForm()

	context = {'form': form}

	return render(request, "content/review.html", context)


@login_required
def flux(request):
	tickets = Ticket.objects.order_by('-id').filter(user_id=request.user.id)

	reviews = Review.objects.order_by('-id').filter(user_id=request.user.id)

	context = {
		'tickets': tickets,
		'reviews': reviews
			   }

	return render(request, "content/flux.html", context)

@login_required
def follow(request):
	if request.method == 'POST':
		form = UserFollowsForm(request.POST)

	else:
		form = UserFollowsForm()

	context = {'form': form}

	return render(request, "content/follow.html", context)


@login_required
def modify_review(request):
	return render(request, "content/modify_review.html")


@login_required
def modify_ticket(request):
	return render(request, "content/modify_ticket.html")


@login_required
def posts(request):
	return render(request, "content/posts.html")
