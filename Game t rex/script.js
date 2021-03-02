var caracter = 
document.getElementById('caracter');

var block = 
document.getElementById('block');

function jump() {
    if (caracter.classList != 'animate') {
        caracter.classList.add('animate');
    }

    setTimeout(function () {
        caracter.classList.remove('animate')
    }, 500)

}

var chechDead = setInterval(function(){
    var caracterTop = 
    parseInt(window.getComputedStyle(caracter).getPropertyValue("top"));

    var BlockLeft = 
    parseInt(window.getComputedStyle(block).getPropertyValue("left"));

    if(BlockLeft<20 && BlockLeft>0 && caracterTop >=130){
        block.style.animation ="none";
        block.style.display ="none";
        alert('loose');
    }


},10);