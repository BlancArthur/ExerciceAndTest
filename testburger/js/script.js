let burgerClose = document.querySelector('.forme');
let burgerClass = document.querySelector('#lourd');
let trait1 = document.querySelector('.trait1');
let trait2 = document.querySelector('.trait2');



burgerClose.addEventListener('click', function (){
    console.log('salut')
    trait1.classList.toggle('cross1')
    trait1.classList.toggle('trait1')
    
    trait2.classList.toggle('cross2')
    trait2.classList.toggle('trait2')
    
})



