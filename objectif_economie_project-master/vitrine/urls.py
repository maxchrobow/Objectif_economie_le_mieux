from django.conf.urls import url
from . import views

urlpatterns = [
	    url(r'^$', views.index, name='index'),  
	    url(r'^isolation/', views.isolation, name='isolation'),
	    url(r'^entretien/', views.entretien, name='entretien'),
	    url(r'^chaudiere/', views.chaudiere, name='chaudiere'),
	    url(r'^pompe_chaleur/', views.pompe_chaleur, name='pompe_chaleur'),
	    url(r'^ballon_thermo/', views.ballon_thermo, name='ballon_thermo'),
	    url(r'^domotique/', views.domotique, name='domotique'),
	    url(r'^mentions_legales/', views.mentions_legales, name='mentions_legales'),
	    url(r'^cee/', views.cee, name='cee'),
	    url(r'^sav/', views.sav, name='sav'),
	    url(r'^contact/', views.contact, name='contact'),
	    url(r'^condition_generale_de_vente/', views.condition_generale_de_vente, name='condition_generale_de_vente'),
	    url(r'^nous_rejoindre/', views.nous_rejoindre, name='nous_rejoindre'),
	    url(r'^page_description_poste/(?P<ma_var>\w+)/', views.page_description_poste, name='page_description_poste'),
		url(r'^description_produit/(?P<ma_var>\w+)/', views.description_produit, name='description_produit'),
	]