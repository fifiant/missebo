function preload_image(a) {
	var b = new Image;
	b.src = a
}

function change_image(d, c) {
	var a = document.getElementById("area_image");
	var b = document.getElementById("county_" + c);
	a.style.backgroundImage = "url(" + d + "/img/map_" + c + ".png)";
	b.style.textDecoration = "underline";
	return true
}

function hide_image(d, c) {
	var a = document.getElementById("area_image");
	var b = document.getElementById("county_" + c);
	a.style.backgroundImage = "url(" + d + "/img/none.gif)";
	b.style.textDecoration = "none";
	return true
}

function add_bookmark() {
	var b = navigator.userAgent.toLowerCase();
	var a = (b.indexOf("konqueror") != -1);
	var c = (b.indexOf("webkit") != -1);
	var e = (b.indexOf("mac") != -1);
	var d = e ? "Command/Cmd" : "CTRL";
	if(window.external && (!document.createTextNode || ( typeof (window.external.AddFavorite) == "unknown"))) {
		window.external.AddFavorite("http://www.leboncoin.fr/", "Petites annonces gratuites d'occasion - leboncoin.fr")
	} else {
		if(a) {alert("Veuillez appuyer sur CTRL + B pour ajouter ce site à vos favoris.")
		} else {
			if(window.opera) {
				void (0)
			} else {
				if(window.home || c) {alert("Veuillez appuyer sur " + d + " + D pour ajouter ce site à vos favoris.")
				} else {
					if(!window.print || e) {alert("Veuillez appuyer sur Command/Cmd + D pour ajouter ce site à vos favoris.")
					} else {alert("Votre navigateur internet n'étant pas reconnu, vous devrez ajouter ce site manuellement à vos favoris.")
					}
				}
			}
		}
	}
};