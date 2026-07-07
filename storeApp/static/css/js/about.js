const words = [
    "Luxury Furniture",
    "Modern Interiors",
    "Elegant Designs",
    "Dream Homes"
];


let i = 0;

setInterval(() => {

    document.getElementById("changing-text").textContent =
    words[i];

    i++;

    if(i >= words.length){
        i = 0;
    }

}, 2000);


const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {

    const updateCounter = () => {

        const target = +counter.getAttribute("data-target");

        const count = parseInt(counter.innerText) || 0;

        const increment = target / 200;

        if (count < target) {

            counter.innerText = Math.ceil(count + increment) + "+";

            setTimeout(updateCounter, 10);

        } else {

            counter.innerHTML = `${target} <span class="plus">+</span>`;

        }

    };

    updateCounter();

});


const reveals =
document.querySelectorAll('.reveal');

window.addEventListener('scroll', () => {

    reveals.forEach(reveal => {

        const windowHeight =
        window.innerHeight;

        const revealTop =
        reveal.getBoundingClientRect().top;

        if(revealTop < windowHeight - 100){

            reveal.classList.add('active');

        }

    });

});


const progressBars =
document.querySelectorAll('.progress-bar');

window.addEventListener('scroll', () => {

    progressBars.forEach(bar => {

        const position =
        bar.getBoundingClientRect().top;

        if(position < window.innerHeight){

            bar.style.width =
            bar.dataset.width;

        }

    });

});