from django.contrib import admin

from .models import *
# Register your models here.

class bdd_devisAdmin(admin.ModelAdmin):
	list_display = ('date_de_demande','sujet','civilite','nom','prenom','titre','adresse','complement_adresse','code_postal','ville','telephone','email','archive')

class bdd_clientAdmin(admin.ModelAdmin):
	list_display = ('date_inscription','civilite','nom','prenom','titre','adresse','complement_adresse','code_postal','ville','telephone','email','archive')

class bdd_postesAdmin(admin.ModelAdmin):
	list_display = ('date_de_publication','titre_du_poste','lieu_du_poste','domaine_activite','type_emploi','horaire_travail','archive')

class bdd_postes_demandeursAdmin(admin.ModelAdmin):
	list_display = ('date_de_demande','titre_du_poste','email','telephone','archive')

class bdd_assistance_techniqueAdmin(admin.ModelAdmin):
	list_display = ('equipement','titre_du_probleme','description_du_probleme','url_video_youtube','solution_du_probleme')

class bdd_produitAdmin(admin.ModelAdmin):
	list_display = ('equipement','titre_du_produit','marque_du_produit','archive')

admin.site.register(bdd_devis,bdd_devisAdmin)
admin.site.register(bdd_client,bdd_clientAdmin)
admin.site.register(bdd_postes, bdd_postesAdmin)
admin.site.register(bdd_postes_demandeurs, bdd_postes_demandeursAdmin)
admin.site.register(bdd_assistance_technique, bdd_assistance_techniqueAdmin)
admin.site.register(bdd_produit, bdd_produitAdmin)