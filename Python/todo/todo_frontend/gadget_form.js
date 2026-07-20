const ADD_URL = 'http://localhost:8000/techgadget/gadgets/add';
const LIST_URL = 'http://localhost:8000/techgadget/gadgets/';

function addGadget() {
    const name = document.getElementById('name').value;
    const category = document.getElementById('category').value;
    const manufacturer = document.getElementById('manufacturer').value;
    const price = document.getElementById('price').value;
    const description = document.getElementById('description').value;

    const gadget = {
        name: name,
        category: category,
        manufacturer: manufacturer,
        price: parseFloat(price),
        currency: 'EUR',
        description: description
    };

    fetch(ADD_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(gadget)
    })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            document.querySelector('.status').textContent = data.message;
            loadGadgets();
        })
        .catch(error => {
            console.error(error);
            document.querySelector('.status').textContent = 'Fehler beim Senden.';
        });
}

function loadGadgets() {
    fetch(LIST_URL)
        .then(response => response.json())
        .then(data => {
            const list = document.querySelector('.gadgetListe');
            list.innerHTML = '';

            data.forEach(gadget => {
                const li = document.createElement('li');
                li.textContent = `${gadget.name} - ${gadget.manufacturer} (${gadget.price} ${gadget.currency})`;
                list.appendChild(li);
            });
        })
        .catch(error => console.error(error));
}
