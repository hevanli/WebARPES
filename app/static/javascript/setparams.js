const liebButton = document.getElementById("lieb-button");
const liebRadio = document.getElementById("lieb-radio");

const triangularButton = document.getElementById("triangular-button");
const triangularRadio = document.getElementById("triangular-radio");

const hexagonalButton = document.getElementById("hexagonal-button");
const hexagonalRadio = document.getElementById("hexagonal-radio");

const kagomeButton = document.getElementById("kagome-button");
const kagomeRadio = document.getElementById("kagome-radio");

const buttons = document.getElementsByClassName('lattice-button');
const radioButtons = document.querySelectorAll('input[name="lattices"]');

const submit = document.getElementById('submit-button');
submit.addEventListener("click", () => {
    console.log(document.querySelector('input[name="lattices"]:checked').value);
    window.location.href = url_for('index');
});

function highlight(button) {
    for (i = 0; i < buttons.length; i++) { buttons[i].style.backgroundColor = ""; }
    button.style.backgroundColor = "hsla(195, 79%, 83%, 0.3)";
    submit.disabled = false;
}

liebButton.addEventListener("click", function() { liebRadio.click(); highlight(liebButton)});
triangularButton.addEventListener("click", function() { triangularRadio.click(); highlight(triangularButton)});
hexagonalButton.addEventListener("click", function() { hexagonalRadio.click(); highlight(hexagonalButton)});
kagomeButton.addEventListener("click", function() { kagomeRadio.click(); highlight(kagomeButton)});