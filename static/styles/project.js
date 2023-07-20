function myFunction() {
  var x = document.getElementById("myLinks");
  console.log("links", x);
  if (x.style.display === "block") {
    x.classList.toggle("displaying");
    x.style.display = "none";
  } else {
    x.style.display = "block";
    x.classList.toggle("displaying");
  }
}
