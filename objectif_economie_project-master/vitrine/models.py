from django.db import models
from django.utils import timezone
from django.forms import ModelForm
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up

# Create your models here.
CHOICES = (('Pompe_a_chaleur','Pompe à chaleur'),
 ('Isolation','Isolation'),
  ('Domotique','Domotique'),
   ('Chaudiere','Chaudiere'),
   ('Ballon_thermodynamique','Ballon thermodynamique'))
#type_reparation = models.CharField(choices=CHOICES,max_length=50, null=True)
#help_text

class bdd_produit(models.Model):

	equipement=models.CharField(choices=CHOICES, max_length=50,null=True)
	marque_du_produit=models.CharField(default=" ",max_length=50)
	titre_du_produit=models.CharField(default=" ",max_length=50)
	image_du_produit=models.ImageField(upload_to='image_produit/')
	premiere_phrases_accroche=models.CharField(default=" ",max_length=100)
	deuxieme_phrases_accroche=models.CharField(default=" ",max_length=100)
	description_detaille_produit=models.TextField(default=" ",max_length=None)

	archive = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Produit"
		ordering = ['equipement','marque_du_produit']

	def __str__(self):
		return self.equipement


class bdd_assistance_technique(models.Model):

	equipement = models.CharField(choices=CHOICES,max_length=50,null=True)
	titre_du_probleme = models.CharField(default=" ", max_length=400)
	description_du_probleme = models.TextField(default=" ",max_length=None)
	solution_du_probleme = models.TextField(default=" ",blank=True,max_length=None)
	url_video_youtube = models.CharField(default=" ",blank=True, max_length=400)

	archive = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Assistance technique"
		ordering = ['equipement']

	def __str__(self):
		return self.equipement

class bdd_client(models.Model):
	civilite = models.CharField(blank=False, default=" ", max_length=400)
	prenom = models.CharField(blank=False, default=" ", max_length=400)
	nom = models.CharField(blank=False, default=" ", max_length=400)
	titre = models.CharField(blank=False, default=" ", max_length=400)
	adresse = models.CharField(blank=False, default=" ", max_length=400)
	complement_adresse = models.CharField(blank=True, max_length=400)
	code_postal = models.CharField(blank=False, default=" ", max_length=400)
	ville = models.CharField(blank=False, default=" ", max_length=400)
	telephone = models.CharField(blank=False, default=" ", max_length=400)
	email = models.CharField(blank=False, default=" ", max_length=400)
	code_parrainage = models.CharField(blank=False, default=" ", max_length=400)
	date_inscription = models.DateTimeField(auto_now_add=True)


	#rajouter une ligne qui est : liste de personne qu'il parraine
	
	archive = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Client"
		ordering = ['nom']

	def __str__(self):
		return self.nom

class bdd_devis(models.Model):
	civilite = models.CharField(blank=False, default=" ", max_length=400)
	prenom = models.CharField(blank=False, default=" ", max_length=400)
	nom = models.CharField(blank=False, default=" ", max_length=400)
	titre = models.CharField(blank=False, default=" ", max_length=400)
	adresse = models.CharField(blank=False, default=" ", max_length=400)
	complement_adresse = models.CharField(blank=True, max_length=400)
	code_postal = models.CharField(blank=False, default=" ", max_length=400)
	ville = models.CharField(blank=False, default=" ", max_length=400)
	telephone = models.CharField(blank=False, default=" ", max_length=400)
	email = models.CharField(blank=False, default=" ", max_length=400)
	date_de_demande = models.DateTimeField(auto_now_add=True)
	sujet = models.CharField(blank=False, default=" ", max_length=400)

	archive = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Devis demande"
		ordering = ['date_de_demande']

	def __str__(self):
		return self.nom


class bdd_postes(models.Model):
	titre_du_poste = models.CharField(blank=False, default=" ", max_length=400)
	description_poste = models.TextField(default=" ",max_length=None)
	lieu_du_poste = models.CharField(blank=False, default=" ", max_length=400)
	domaine_activite = models.CharField(blank=False, default=" ", max_length=400)
	type_emploi = models.CharField(blank=False, default=" ", max_length=400)
	horaire_travail = models.CharField(blank=False, default=" ", max_length=400)


	date_de_publication = models.DateField(auto_now_add=True)

	archive = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Poste"
		ordering = ['date_de_publication']

	def __str__(self):
		return self.titre_du_poste

class bdd_postes_demandeurs(models.Model):
	titre_du_poste = models.CharField(blank=False, default=" ", max_length=400)
	telephone = models.CharField(blank=False, default=" ", max_length=400)
	email = models.CharField(blank=False, default=" ", max_length=400)
	date_de_demande = models.DateField(auto_now_add=True)
	cv = models.FileField(upload_to='cv_demande/')

	archive = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Poste demandeur"
		ordering = ['date_de_demande']

	def __str__(self):
		return self.titre_du_poste