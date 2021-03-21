

const blogs = document.querySelectorAll('.blog');
const input = document.querySelector('.search');

input.addEventListener('keyup', e => search(e, blogs))

// ! Modified by Hamza (Added toLowerCase)

const search =  (e, nodes) => {
  nodes.forEach((node) => {
    if (!node.dataset.search.trim().toLowerCase().includes(e.target.value.toLowerCase())) {
      node.classList.add('filter');
    } else {
      node.classList.remove('filter');
    }
  })
}

