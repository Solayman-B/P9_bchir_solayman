from django.test import TestCase

# Create your tests here.
"""class SubscriberForm(foms.Form):  # ou forms.ModelForm

	# description du formualre

	def __init__(self, user, *args, **kwargs):
		#Modifier l'initialisation pour recevoir l'utilisateur à l'intenciation
		#du formulaire.
		
		self.user = user
		super().__init__(*args, **kwargs)

	def clean_followed_user(self):
		#Validation du champ followed_user
		#avec récupération de l'utilisateur en base.
		
		# on récupère le username de l'utilisateur suivi
		username = self.cleaned_data['followed_user']
		try:
			# on cherche l'utilisateur dans la base
			user = User.objects.get(username=username)
		except User.DoesNotExist:
			# si on ne trouve pas l'utilisateur, erreur de validation
			raise ValidationErreur("Utilisateur inconnu !")
		return user

	def save(self, commit=True):
		#Crée et sauvegarde une nouvelle instance de subscriber.
		
		subscriber = Subscriber(
			user="ajouter ici l'utilisateur courant",
			followed_user=self.cleaned_data['followed_user']
		)
		if commit:
			subscriber.save()
		return subscriber"""