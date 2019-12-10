from django import forms

from .models import *

class bdd_postes_demandeursForm(forms.ModelForm):
	class Meta:
		model = bdd_postes_demandeurs
		fields = ('cv',)
		widgets = {
            'cv': forms.FileInput(attrs={'class': 'input-format-file'}),
        }

class bdd_produitForm(forms.ModelForm):
	class Meta:
		model=bdd_produit
		fields=('image_du_produit',)
		widgets = {
            'image_du_produit': forms.FileInput(),
        }
