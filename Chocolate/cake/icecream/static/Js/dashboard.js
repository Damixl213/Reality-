const SideMenue= document.querySelector("aside");
const MenueBtn= document.querySelector("#menu-btn");
const closeBtn= document.querySelector("#close-btn");
const themeToggler= document.querySelector(".theme-toggler")
const active= document.querySelector(".moon")
const disactive= document.querySelector(".Sun")

// To show  sidebar
MenueBtn.addEventListener('click',()=>{
  SideMenue.style.display='block';
})
// To close sidebar
closeBtn.addEventListener('click', ()=>{
  SideMenue.style.display='none';
})

// change theme
themeToggler.addEventListener('click',() =>{
  document.body.classList.toggle('dark-theme-varibles');
})

disactive.addEventListener('click', ()=>{
   active.style.display='block'
   disactive.style.display='none'
})

active.addEventListener('click', ()=>{
   active.style.display='none'
   disactive.style.display='block'
})