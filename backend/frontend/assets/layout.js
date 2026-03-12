async function loadLayout(){

try{

const header = await fetch("/layout/header.html")
const sidebar = await fetch("/layout/sidebar.html")
const footer = await fetch("/layout/footer.html")

const headerHTML = await header.text()
const sidebarHTML = await sidebar.text()
const footerHTML = await footer.text()

const headerEl = document.getElementById("header")
const sidebarEl = document.getElementById("sidebar")
const footerEl = document.getElementById("footer")

if(headerEl) headerEl.innerHTML = headerHTML
if(sidebarEl) sidebarEl.innerHTML = sidebarHTML
if(footerEl) footerEl.innerHTML = footerHTML

}catch(err){

console.error("Layout load failed:", err)

}

}

document.addEventListener("DOMContentLoaded", loadLayout)