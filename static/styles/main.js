const letters = document.querySelectorAll(".letter");
const word = document.querySelector(".word");
const hidden = document.querySelectorAll(".hidden");
const imageContainer = document.querySelectorAll(".img-container");
let imageContainer1 = imageContainer[0];
// alert("I AM THE APP.JS FILE");

function ranColor() {
  let r = Math.floor(Math.random() * 256);
  let g = Math.floor(Math.random() * 256);
  let b = Math.floor(Math.random() * 256);

  return `rgb(${r},${g},${b})`;
}

function colorSetting() {
  let x = setInterval(() => {
    for (let letter of letters) {
      let newColor = ranColor();
      setColor(letter, newColor);
    }
  }, 1000);
}

function setColor(element, color) {
  element.style.color = color;
}

function mouseOver(evt) {
  //console.log(evt.target);
  if (evt.target.nodeName === "SPAN") {
    evt.target.classList.add("pointing");
    console.log(evt.target);
    word.addEventListener("click", handleClick);
  }
}

function handleClick(evt) {
  //console.log(evt.target.parentElement);
  const div = evt.target.parentElement;
  div.classList.toggle("clicked");
}

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    console.log(entry);
    if (entry.isIntersecting) {
      entry.target.classList.add("show");
    } else {
      entry.target.classList.remove("show");
    }
  });
});

hidden.forEach((el) => observer.observe(el));

async function getDog() {
  const data = await axios({
    url: "https://dog.ceo/api/breeds/image/random",
    method: "GET",
  });
  console.log(data.data.message);
  const img = document.querySelectorAll("img");
  for (let i of img) {
    i.src = data.data.message;
  }
  console.log(img);
  console.log(img.src);
  return img;
}

function mouseIn(e) {
  console.log("mouseIn", e.target);
}
function mouseOut(e) {
  console.log("mouseOut", e.target);
  e.target.classList.add("hover");
}
document.addEventListener("DOMContentLoaded", colorSetting);
document.addEventListener("DOMContentLoaded", getDog);
document.addEventListener("mouseover", mouseOver);
imageContainer1.addEventListener("mouseenter", mouseIn);
imageContainer1.addEventListener("mouseleave", mouseOut);
