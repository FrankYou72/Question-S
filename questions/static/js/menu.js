function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
  const imgs = document.getElementsByClassName('slideImage')
  for (let img of imgs) {
      img.style.marginLeft = '4%'
  }
  console.log(imgs)
}

/* Set the width of the side navigation to 0 and the left margin of the page content to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
  const imgs = document.getElementsByClassName('slideImage')
  for (let img of imgs) {
      img.style.marginLeft = '11.5%'
  }
}