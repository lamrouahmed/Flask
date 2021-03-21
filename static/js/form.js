const labels = document.querySelectorAll('.label');
const spans = document.querySelectorAll('.border');
const inputs = document.querySelectorAll('.input');

labels.forEach((label, index) => label.addEventListener('click', () => addBorder(index)))
inputs.forEach((input, index) => input.addEventListener('focus', () => addBorder(index)))

window.addEventListener('click', e => removeBorder(e,'input'))


const removeBorder = (e, className) => {
    if (!e.target.className.includes(className)) {
        spans.forEach(span => span.classList.remove('clicked'))
    } 
}
const addBorder = index => {
    spans.forEach(span => span.classList.remove('clicked'))
    spans[index].classList.add('clicked');
}