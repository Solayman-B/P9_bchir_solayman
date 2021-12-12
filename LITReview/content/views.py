from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket, Review, UserFollows
from .forms import TicketForm, ReviewForm, SubscribingForm


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
										   headline=form.cleaned_data.get('headline'),
										   rating=form.cleaned_data.get('rating'),
										   body=form.cleaned_data.get('body'),
										   ticket=ticket)
			return redirect('content:flux')
	else:
		form = ReviewForm()

	context = {
		'ticket': ticket,
		'form': form
	}

	return render(request, "content/ticket_detail.html", context)


@login_required
def ticket_update(request, ticket_id):
	ticket = Ticket.objects.get(id=ticket_id)

	if request.method == 'POST':
		form = TicketForm(request.POST, instance=ticket)
		if form.is_valid():
			form.save()
			return redirect('content:posts')
	else:
		form = TicketForm(instance=ticket)
	context = {'form': form}

	return render(request, "content/ticket_update.html", context)


@login_required
def review(request):
	if request.method == 'POST':
		review_form = ReviewForm(request.POST)
		ticket_form = TicketForm(request.POST)

		if review_form.is_valid() and ticket_form.is_valid():
			ticket = Ticket.objects.create(user_id=request.user.pk, title=ticket_form.cleaned_data.get('title'),
										   description=ticket_form.cleaned_data.get('description'))

			review = Review.objects.create(user_id=request.user.pk,
										   headline=review_form.cleaned_data.get('headline'),
										   rating=review_form.cleaned_data.get('rating'),
										   body=review_form.cleaned_data.get('body'),
										   ticket=ticket)
			return redirect('content:flux')
	else:
		review_form = ReviewForm()
		ticket_form = TicketForm()

	context = {
		'review_form': review_form,
		'ticket_form': ticket_form
	}

	return render(request, "content/review.html", context)


@login_required
def review_update(request, review_id):
	review = Review.objects.get(id=review_id)
	ticket = Ticket.objects.get(id=review.ticket_id)

	if request.method == 'POST':
		form = ReviewForm(request.POST, instance=review)
		if form.is_valid():
			form.save()
			return redirect('content:posts')
	else:
		form = ReviewForm(instance=review)

	context = {
		'ticket': ticket,
		'form': form,
	}

	return render(request, "content/review_update.html", context)


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
		subscribing_form = SubscribingForm(request.POST)
		return redirect('content:flux')

	else:
		subscribing_form = SubscribingForm()

	user_following = UserFollows.objects.filter(user=request.user)
	user_followed_by = UserFollows.objects.filter(user=request.user)

	context = {
		'subscribing_form': subscribing_form,
		'user_following': user_following,
		'user_followed_by': user_followed_by
	}

	return render(request, "content/follow.html", context)


@login_required
def posts(request):
	tickets = Ticket.objects.order_by('-id').filter(user_id=request.user.id)

	reviews = Review.objects.order_by('-id').filter(user_id=request.user.id)

	context = {
		'tickets': tickets,
		'reviews': reviews
	}
	return render(request, "content/posts.html", context)

@login_required
def ticket_delete(request, ticket_id):
	ticket = Ticket.objects.get(id = ticket_id)

	if request.method == 'POST':
		ticket.delete()
		return redirect('content:posts')

	context = {
		'ticket':ticket
	}
	return render(request, "content/ticket_delete.html", context)

@login_required
def review_delete(request, review_id):
	review = Review.objects.get(id = review_id)

	if request.method == 'POST':
		review.delete()
		return redirect('content:posts')

	context = {
		'review':review
	}
	return render(request, "content/review_delete.html", context)