from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from accounts.models import User
from .models import Ticket, Review, UserFollows
from .forms import TicketForm, ReviewForm
from itertools import chain
#from django.db.models import Q



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

def followed_users_objects(users):
	object = []
	for user in users:
		object.append(list(chain(Ticket.objects.filter(user_id=user.abonnements_id).annotate(content_type=Value('TICKET', CharField())), Review.objects.filter(user_id=user.abonnements_id).annotate(content_type=Value('REVIEW', CharField())))))
	objects = list(chain.from_iterable(object))
	return objects

@login_required
def flux(request):
	user_tickets = Ticket.objects.filter(user_id=request.user.id)
	user_tickets = user_tickets.annotate(content_type=Value('USER_TICKET', CharField()))
	user_reviews = Review.objects.filter(user_id=request.user.id)
	user_reviews = user_reviews.annotate(content_type=Value('USER_REVIEW', CharField()))
	users = UserFollows.objects.filter(abonnes_id=request.user.id)
	followed_objects = followed_users_objects(users)

	posts = sorted(
		chain(user_tickets, user_reviews, followed_objects),
		key=lambda post: post.time_created,
		reverse=True
	)

	return render(request, "content/flux.html", context={'posts': posts})


@login_required
def follow(request):
	if request.POST.get('search'):
		users = User.objects.filter(username__iexact=request.POST.get('search'))
		new_abonne = users.first()
		userf = UserFollows.objects.create(abonnes=request.user, abonnements=new_abonne)

	abonnes = UserFollows.objects.filter(abonnes_id=request.user)
	abonnements = UserFollows.objects.filter(abonnements_id=request.user)

	context = {
		'abonnes': abonnes,
		'abonnements': abonnements,
	}

	return render(request, "content/follow.html", context)


@login_required
def unfollow(request, follow_id):
	unfollow = UserFollows.objects.get(id=follow_id)

	if request.method == 'POST':
		unfollow.delete()
		return redirect('content:follow')

	context = {
		'unfollow': unfollow,
	}

	return render(request, "content/unfollow.html", context)


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