// generate the orbital energy inputs dynamically based on selected orbital level
function displayInputs() {
    // remove current inputs on the page so you don't get duplicates
    inputs = document.getElementsByClassName('orbital-energy');
    while (inputs.length > 0) { inputs[0].parentNode.removeChild(inputs[0]); }

    // adds the appropriate number of text inputs to each group
    groups = document.getElementsByClassName('selection-group');
    for (let i = 0; i < groups.length; i++) {
        const selector = groups[i].querySelector('.form-control');

        let x;
        if (selector.value == 's') x = 1;
        else if (selector.value == 'p') x = 3;
        else if (selector.value == 'd') x = 5;
        else if (selector.value == 'f') x = 7;

        for (let j = 0; j < x; j++) {
            const input = document.createElement("input");
            input.type = "text";
            input.className = "orbital-energy form-control"
            groups[i].appendChild(input);
        }
    }
}

// on change event listeners
selectors = document.getElementsByClassName('form-control');
for (let i = 0; i < selectors.length; i++) {
    selectors[i].addEventListener("change", displayInputs);
}

// call display inputs so they show up on page load
displayInputs();