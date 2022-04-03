const container = document.querySelector('.container')

container.addEventListener('click',()=>{
    alert('welcome to my first hosted api site')
})
window.addEventListener('scroll',()=>{
    container.classList.toggle('hi')
})