function Menu() {
	var top_nav = document.getElementById("top-navi");
	if (top_nav.className === "top-navi"){
		top_nav.className += " toggle-open";
		icon.innerHTML = "&#10005; Close Menu";
	} else{
		top_nav.className = "top-navi";
		icon.innerHTML = "&#9776; Menu";
	}
}