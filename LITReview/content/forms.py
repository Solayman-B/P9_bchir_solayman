from django import forms
from .models import Ticket, Review, UserFollows


class TicketForm(forms.ModelForm):
	title = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control', }))
	description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', }), required=False)

	class Meta:
		model = Ticket
		fields = ['title', 'description']

class ReviewForm(forms.ModelForm):
	title = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control', }))
	description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', }), required=False)
	headline = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control', }))
	rating = forms.ChoiceField(choices=[(i, i) for i in range(0, 6)], widget=forms.RadioSelect())
	body = forms.CharField(label='Commentaire', widget=forms.Textarea(attrs={'class': 'form-control', }), required=False)

	class Meta:
		model = Review
		fields = ['title', 'description', 'headline', 'rating', 'body']

class TicketDetailForm(forms.ModelForm):
	headline = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control', }))
	rating = forms.ChoiceField(choices=[(i, i) for i in range(0, 6)], widget=forms.RadioSelect())
	body = forms.CharField(label='Commentaire', widget=forms.Textarea(attrs={'class': 'form-control', }))

	class Meta:
		model = Review
		fields = ['headline', 'rating', 'body']

class UserFollowsForm(forms.ModelForm):
	user = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
	followed_user = forms.CharField(label="Abonnements", widget=forms.TextInput(attrs={'class': 'form-control', }))
	class Meta:
		model = UserFollows
		fields = ['user', 'followed_user']
