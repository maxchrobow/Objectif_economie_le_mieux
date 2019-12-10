from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import *
from django.contrib import messages
from .forms import *

# Create your views here.
def contact(request):

	if request.POST.get('submit_devis'):
		bdd_devis(civilite=request.POST.get('civilite'),
			nom=request.POST.get('nom').lower(),
			prenom=request.POST.get('prenom').lower(),
			titre=request.POST.get('titre'),
			adresse=request.POST.get('adresse'),
			complement_adresse=request.POST.get('complement_adresse'),
			code_postal=request.POST.get('code_postal'),
			ville=request.POST.get('ville'),
			telephone=request.POST.get('telephone'),
			email=request.POST.get('email'),
			sujet=request.POST.get('sujet')).save()
		messages.success(request,'Votre demande à bien été envoyée et serra traitée sous 48h.')
		return HttpResponseRedirect('/contact')

	if request.POST.get('submit_parrainage'):
		nom_du_parrain = request.POST.get('nom').lower()
		prenom_du_parrain = request.POST.get('prenom').lower()
		code_du_parrain = request.POST.get('code')
		for clients in bdd_client.objects.all():
			if(clients.nom.lower() == nom_du_parrain and clients.prenom.lower() == prenom_du_parrain and clients.code_parrainage == code_du_parrain):
				messages.success(request,'Votre parrain à bien été enregistré, vous pouvez continuer vos recherches sur le site.')
				return HttpResponseRedirect('/contact')
		messages.error(request,'Les informations qui vous avez remplis ne correspondent pas avec nos donnés, nous n\'avons pas réussi à trouver votre parrain. Veuillez ré-essayer')
		return HttpResponseRedirect('/contact')

	liste_probleme = bdd_assistance_technique.objects.filter(archive=False)
	context = locals()
	template = "contact.html"
	return render(request,template,context)

def nous_rejoindre(request):

	if request.POST.get('submit_poste'):
		formulaire_cv = bdd_postes_demandeursForm(request.POST, request.FILES)
		if formulaire_cv.is_valid():
			post_cv = formulaire_cv.save(commit=False)
			post_cv.telephone = request.POST.get('telephone')
			post_cv.email = request.POST.get('email')
			post_cv.titre_du_poste = request.POST.get('titre_du_poste')
			post_cv.save()

			messages.success(request,'Merci d\'avoir postulé. Vous recevrez une réponse d\'ici deux jours ouvrés.')
		return HttpResponseRedirect('/nous_rejoindre')
	else:	
		formulaire_cv = bdd_postes_demandeursForm()

	liste_poste = bdd_postes.objects.filter(archive=False)
	context = locals()
	template = "nous_rejoindre.html"
	return render(request,template,context)

def description_produit(request,ma_var):
	
	produit = bdd_produit.objects.get(id=ma_var)

	context = locals()
	template = 'description_produit.html' 
	return render(request,template,context)

def page_description_poste(request,ma_var):
	
	poste = bdd_postes.objects.get(id=ma_var)

	context = locals()
	template = 'page_description_poste.html'
	return render(request,template,context)

def condition_generale_de_vente(request):
	context = locals()
	template = "condition_generale_de_vente.html"
	return render(request,template,context)
	
def index(request):
	page_color="#6f2525;"
	context = locals()
	template = "index.html"
	return render(request,template,context)

def isolation(request):
	context = locals()
	template = "isolation.html"
	return render(request,template,context)

def entretien(request):
	context = locals()
	template = "entretien.html"
	return render(request,template,context)

def chaudiere(request):
	page_color="#8e7762;"
	context = locals()
	template = "chaudiere.html"
	return render(request,template,context)

def pompe_chaleur(request):
	
	liste_produit=bdd_produit.objects.filter(archive=False)
	page_color="#356f20;"
	context = locals()
	template = "pompe_chaleur.html"
	return render(request,template,context)

def ballon_thermo(request):
	page_color="#00449e;"
	context = locals()
	template = "ballon_thermo.html"
	return render(request,template,context)
	
def domotique(request):
	page_color="#c9b166;"
	context = locals()
	template = "domotique.html"
	return render(request,template,context)

def mentions_legales(request):
	context = locals()
	template = "mentions_legales.html"
	return render(request,template,context)

def cee(request):
	context = locals()
	template = "cee.html"
	return render(request,template,context)

def sav(request):
	context = locals()
	template = "sav.html"
	return render(request,template,context)