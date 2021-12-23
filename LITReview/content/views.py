from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value
from accounts.models import User
from .models import Ticket, Review, UserFollows
from .forms import TicketForm, ReviewForm
from itertools import chain



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

def followed_users_objects(users_follow, request):
	object = []
	for user_follow in users_follow:
		object.append(list(chain(Ticket.objects.filter(user_id=user_follow.abonnements_id).annotate(content_type=Value('TICKET', CharField())), Review.objects.filter(user_id=user_follow.abonnements_id).annotate(content_type=Value('REVIEW', CharField())))))
	objects = list(chain.from_iterable(object))
	return objects

@login_required
def flux(request):
	user_tickets = Ticket.objects.filter(user_id=request.user.id)
	test = Review.objects.filter(user_id=request.user.id)
	print('test', test)
	#test2 = Ticket.objects.filter(id__in=test.ticket_id)

	for test3 in test:
		print(Ticket.objects.filter(id__in=test3.ticket_id), 'SOLUTION')

	Ticket.objects.filter(id = Review.objects.filter(user_id=request.user.id))

	user_tickets = user_tickets.annotate(content_type=Value('USER_TICKET', CharField()))

	user_reviews = Review.objects.filter(user_id=request.user.id)
	user_reviews = user_reviews.annotate(content_type=Value('USER_REVIEW', CharField()))

	users_follow = UserFollows.objects.filter(abonnes_id=request.user.id)

	response_review = Review.objects.exclude(user_id=request.user.id)
	response_review = response_review.filter(ticket__in = Ticket.objects.filter(user_id=request.user.id))
	response_review = response_review.annotate(content_type=Value('REVIEW', CharField()))

	followed_objects = followed_users_objects(users_follow, request)

	followed_objects_cleaned = []
	for followed_object in followed_objects:
		if followed_object not in response_review:
			followed_objects_cleaned.append(followed_object)

	posts = sorted(
		chain(user_tickets, user_reviews, followed_objects_cleaned, response_review),
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
	user_tickets = Ticket.objects.filter(user_id=request.user.id)
	user_tickets = user_tickets.annotate(content_type=Value('USER_TICKET', CharField()))
	user_reviews = Review.objects.filter(user_id=request.user.id)
	user_reviews = user_reviews.annotate(content_type=Value('USER_REVIEW', CharField()))
	response_review = Review.objects.filter(user_id=request.user.id) # A FINIR LNVLZNVIZNVILZNDVLINZDLVNZLKN
	response_review = response_review.annotate(content_type=Value('REVIEW', CharField()))

	posts = sorted(
		chain(user_tickets, user_reviews, response_review),
		key=lambda post: post.time_created,
		reverse=True
	)

	return render(request, "content/posts.html", context={'posts': posts})

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