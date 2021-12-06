from dal import autocomplete
from django import forms
from .models import Ticket, Review, UserFollows


class TicketForm(forms.ModelForm):
	title = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control', }))
	description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', }))

	class Meta:
		model = Ticket
		fields = ['title', 'description']


class ReviewForm(forms.ModelForm):
	title = Ticket.reviews
	description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', }))
	headline = forms.CharField(label='Titre')
	rating = forms.ChoiceField(choices=[(i, i) for i in range(0, 6)], widget=forms.RadioSelect())
	edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)
	body = forms.CharField(label='Commentaire')

	class Meta:
		model = Review
		fields = ['headline', 'rating', 'body']


class UserFollowsForm(forms.ModelForm):
	user = forms.CharField()#label="", widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
	#followed_user = forms.CharField(label="Abonnements", widget=forms.TextInput(attrs={'class': 'form-control', }))
	class Meta:
		model = UserFollows
		fields = ['user', 'followed_user']
		widgets= {
			'user': autocomplete.ModelSelect2(url = 'content:user_autocomplete'),
		}
