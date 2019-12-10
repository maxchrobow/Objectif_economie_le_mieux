var etape = 0;

function make_grey(n){
	var i;
	var x = document.getElementsByClassName("bouton-sujet");

	for (i=0; i < 5; i++)
	{
		if(i == n)
		{
			x[i].className = "bouton-sujet active";
			nextPrev(1);
		}
		else
		{
			x[i].className = "bouton-sujet inactive";
		}
	}
}

function nextPrev(n) {
  // Determine quelle section afficher

  if (etape == 0)
  {
  	if(n == -1)
  	{
  		return;
  	}
  	etape = 1;
	    var x = document.getElementsByClassName("bouton-sujet");//Tous les boutons sujet step1
	    var y = document.getElementsByClassName("step2");//Toutes les sections associés aux boutons sujet step2
	    var i;
	    for (i=0; i < 2; i++)//recherche quel bouton sujet est actif dans les 2 premiers(l'animation change pour les 3 derniers)
	{
		if(x[i].classList.contains("active"))
		{
			document.getElementById("step1").classList = "out_d_g";//lance l'animation sur les boutons sujet step1
			//display block la section associé au bouton sujet actif
			setTimeout(function(y,i){document.getElementById("step1").classList = "display-none";
			y[i].classList = "step2 display-block-bouton display-block in_d_g";},200,y,i);//display none les boutons sujet step1
			setTimeout(function(y,i){y[i].classList = "step2 display-block-bouton display-block";},1000,y,i);
			return;
		}
	}
	for (i=2; i < 5; i++)//même principe qu'au dessus mais avec une animation differente pour les 3 derniers boutons
	{
		if(x[i].classList.contains("active"))
		{
			document.getElementById("TEST").classList ="test animate_content";//display none la page entiere
			setTimeout(function(y,i){y[i].classList = "step2 display-block-form";//display block le formulaire
				document.getElementById("step1").classList = "display-none";//display none les boutons sujet step1
				document.getElementById("TEST").classList ="test-form";},400,y,i);//display block la page entiere apres 0.4 s
			return;
		}
	}
	etape = 0;//si aucun bouton n'était actif on reste a l'étape 0
	return;
  }

  else if (etape == 1)
  {
  	if(n == -1)//retour en arrière étape 1
  	{
  		etape = etape - 1;
  		var y = document.getElementsByClassName("step2");//Toutes les sections en étape 2
  		var i;
  		for (i=0; i < 2; i++)//recherche la section display block dans l'étape 2 pour les 2 premiere section
		{
			if(y[i].classList.contains("display-block-bouton"))
			{
				var a = y[i];
				a.classList = "display-block-bouton out_g_d";//lance l'animation sur les boutons step2
				document.getElementById("step1").classList = "step1 display-block in_g_d";//display block les boutons sujet step1
				setTimeout(function(){a.classList = "step2 display-none";},500,a);//display none les boutons step2
				return;
			}
		}
		for (i=2; i < 5; i++)//même principe qu'au dessus mais avec les 3 derniere sections
		{
			if(y[i].classList.contains("display-block-form"))
			{
				document.getElementById("TEST").classList ="test animate_content";//display none la page entiere
				setTimeout(function(y,i){y[i].classList = "step2 display-none-form";//display none le formulaire
						document.getElementById("step1").classList = "display-block";//display block les boutons sujet step1
						document.getElementById("TEST").classList ="test";},400,y,i);//display block la page entiere apres 0.4 s
				return;
			}
		}
  	}
  }
}
function confirmEmail() {
    var email = document.getElementById("email").value
    var confemail = document.getElementById("confemail").value
    if(email != confemail) {
        alert('L\'email ne correspond pas!');
    }
}