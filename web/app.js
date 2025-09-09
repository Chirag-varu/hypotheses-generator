const factForm = document.getElementById('factForm');
const factInput = document.getElementById('factInput');
const factsList = document.getElementById('factsList');
const generateBtn = document.getElementById('generateBtn');
const output = document.getElementById('output');

let facts = [];

factForm.addEventListener('submit', function(e) {
    e.preventDefault();
    const fact = factInput.value.trim();
    if (fact) {
        facts.push(fact);
        renderFacts();
        factInput.value = '';
    }
});

generateBtn.addEventListener('click', function() {
    output.textContent = 'Generating hypotheses...';
        fetch('http://127.0.0.1:5000/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ facts })
    })
    .then(res => res.json())
    .then(data => {
        output.textContent = data.result || 'No hypotheses generated.';
    })
    .catch(() => {
        output.textContent = 'Error contacting backend.';
    });
});


function renderFacts() {
    factsList.innerHTML = '';
    facts.forEach((f, idx) => {
        const li = document.createElement('li');
        li.style.display = 'flex';
        li.style.alignItems = 'center';
        const span = document.createElement('span');
        span.textContent = f;
        li.appendChild(span);
        const delBtn = document.createElement('button');
        delBtn.textContent = 'Delete';
        delBtn.style.marginLeft = '10px';
        delBtn.style.background = '#f87171';
        delBtn.style.color = '#fff';
        delBtn.style.border = 'none';
        delBtn.style.borderRadius = '4px';
        delBtn.style.cursor = 'pointer';
        delBtn.onclick = function() {
            facts.splice(idx, 1);
            renderFacts();
        };
        li.appendChild(delBtn);
        factsList.appendChild(li);
    });
}

// Clear all facts button
const clearFactsBtn = document.getElementById('clearFactsBtn');
clearFactsBtn.addEventListener('click', function() {
    facts = [];
    renderFacts();
});
