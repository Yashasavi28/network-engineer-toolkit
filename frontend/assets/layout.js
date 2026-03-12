async function loadLayout(){

const header = await fetch("/layout/header.html")
const sidebar = await fetch("/layout/sidebar.html")
const footer = await fetch("/layout/footer.html")

document.getElementById("header").innerHTML = await header.text()
document.getElementById("sidebar").innerHTML = await sidebar.text()
document.getElementById("footer").innerHTML = await footer.text()

}

loadLayout()