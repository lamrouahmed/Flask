

const blogs = document.querySelectorAll('.blog');
const input = document.querySelector('.search');

input.addEventListener('keyup', e => search(e, blogs))


const search =  (e, nodes) => {
  nodes.forEach((node) => {
    if (!node.dataset.search.trim().includes(e.target.value)) {
      node.classList.add('filter');
    } else {
      node.classList.remove('filter');
    }
  })
}

