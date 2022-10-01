let text = document.getElementById("text-box");
let str = text.innerHTML;

text.innerHTML = "";

let speed = 20;
let i = 0;

function typeWriter() {
    if (i < str.length) {
        text.innerHTML += str.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
    }
}

setTimeout(typeWriter, speed);
