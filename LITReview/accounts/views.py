from .forms import UserForm
from django.shortcuts import render, redirect


def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = UserForm()

    context = {
        "form": form,
    }

    return render(request, "accounts/register.html", context)
