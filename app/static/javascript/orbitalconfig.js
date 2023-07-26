// orbital input labels
const p = ["p<sub>x</sub>", "p<sub>z</sub>", "p<sub>y</sub>"];
const d = ["d<sub>xy</sub>", "d<sub>xz</sub>", "d<sub>z<sup>2</sup></sub>", "d<sub>yz</sub>", "d<sub>x<sup>2</sup>-y<sup>2</sup></sub>"];
const f = ["f<sub>x(x<sup>2</sup>-3y<sup>2</sup>)</sub>", "f<sub>y(x<sup>2</sup>-z<sup>2</sup>)</sub>", "f<sub>xz<sup>2</sup></sub>", "f<sub>z<sup>3</sup></sub>", "f<sub>yz<sup>2</sup></sub>", "f<sub>xyz</sub>", "f<sub>y(3x<sup>2</sup>-y<sup>2</sup>)</sub>"]

// generate the orbital energy inputs dynamically based on selected orbital level
function displayInputs() {
    // remove current inputs on the page so you don't get duplicates
    removeDivs();

    // adds the appropriate number of text inputs to each group
    groups = document.getElementsByClassName('selection-group');
    for (let i = 0; i < groups.length; i++) {
        const selector = groups[i].querySelector('.form-control');

        let x;
        if (selector.value == 's') x = 1;
        else if (selector.value == 'p') x = 3;
        else if (selector.value == 'd') x = 5;
        else if (selector.value == 'f') x = 7;

        if (x == 1) groups[i].append(createDiv(i, 0, "s")); 
        else if (x == 3) for (let j = 0; j < x; j++) { groups[i].append(createDiv(i, j, p[j])); }
        else if (x == 5) for (let j = 0; j < x; j++) { groups[i].append(createDiv(i, j, d[j])); }
        else if (x == 7) for (let j = 0; j < x; j++) { groups[i].append(createDiv(i, j, f[j])); }

    }
}
// create input labels
function createLabel(i, num, inner) {
    const label = document.createElement("label");
    label.htmlFor = "input-"+i+"-"+num;
    label.innerHTML = inner+" ";
    label.style.display = "inline-block";
    return label;
}
// create input fields
function createInput(i, num) {
    const input = document.createElement("input");
    input.type = "float";
    input.className = "orbital-energy form-control"
    input.required = true;
    input.name = "orbital-energy-"+i+"-"+num;
    input.id = "input-"+i+"-"+num;
    input.style.display = "inline-block";
    return input;
}
// create divs to group label and input
function createDiv(i, num, inner) {
    div = document.createElement("div");
    div.appendChild(createLabel(i, num, inner));
    div.appendChild(createInput(i, num));
    div.className = "input-div";
    return div;
}
// remove divs currently on DOM
function removeDivs() {
    divs = document.getElementsByClassName('input-div');
    while (divs.length > 0) {
        while (divs[0].firstChild) divs[0].removeChild(divs[0].firstChild);
        divs[0].parentNode.removeChild(divs[0]);
    }
}

// on change event listeners for dropdowns
selectors = document.getElementsByClassName('form-control');
for (let i = 0; i < selectors.length; i++) {
    selectors[i].addEventListener("change", displayInputs);
}

// call display inputs so they show up on page load
displayInputs();