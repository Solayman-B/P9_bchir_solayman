from django.shortcuts import render


def flux(request):
	return render(request, "content/flux.html")


def review(request):
	return render(request, "content/review.html")


def follow(request):
	return render(request, "content/follow.html")


def modify_review(request):
	return render(request, "content/modify_review.html")


def modify_ticket(request):
	return render(request, "content/modify_ticket.html")


def posts(request):
	return render(request, "content/posts.html")


def ticket(request):
	return render(request, "content/ticket.html")
