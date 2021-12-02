from django import forms
from .models import Ticket, Review

class TicketForm(forms.ModelForm):
	title = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control', }))
	description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', }))
	class Meta:
		model = Ticket
		fields = ['title', 'description']


class ReviewForm(forms.ModelForm):
	title = Ticket.reviews #forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control', }))
	description = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', }))
	headline = forms.CharField(label='Titre')
	#rating =
	body = forms.CharField(label='Commentaire')
	class Meta:
		model = Review
		fields = ['headline', 'body']