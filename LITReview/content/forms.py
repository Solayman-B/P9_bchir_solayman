from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
	title = forms.CharField(label='Titre', widget=forms.TextInput(attrs={'class': 'form-control', }))
	content = forms.CharField(label='Description', widget=forms.Textarea(attrs={'class': 'form-control', }))
	class Meta:
		model = Ticket
		fields = '__all__'