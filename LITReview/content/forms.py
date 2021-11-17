from django import forms

class Ticket(forms.ModelForm):
	class Meta:
		fields = ['title', 'content']