function addItemToCart(itemId) {
    const item = document.getElementById(itemId);
    const itemName = item.querySelector('h3').innerText;
    const itemPrice = item.querySelector('p:nth-of-type(2)').innerText;
    const itemDesc = item.querySelector('p:nth-of-type(3)').innerText;

    const cartItem = { name: itemName, price: itemPrice, description: itemDesc };
    let cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.push(cartItem);
    localStorage.setItem('cart', JSON.stringify(cart));
    showCart();
}

function showCart() {
    const cartList = document.getElementById('cart');
    const cart = JSON.parse(localStorage.getItem('cart')) || [];

    cartList.innerHTML = '';

    cart.forEach((item, index) => {
        const li = document.createElement('li');
        const img = document.createElement('img');
                img.src = item.image;
                img.alt = item.name;
                img.width = 100;
                li.appendChild(img);
        const itemName = document.createElement('h2');
        itemName.textContent = item.name;
        li.appendChild(itemName);

        const itemPrice = document.createElement('p');
        itemPrice.textContent = item.price;
        li.appendChild(itemPrice);

        const itemDesc = document.createElement('p');
        itemDesc.textContent = item.description;
        li.appendChild(itemDesc);

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.onclick = function() {
            removeFromCart(index);
        };
        li.appendChild(deleteBtn);

        const buyBtn = document.createElement('button');
        buyBtn.textContent = 'Buy Now';
        // Handle buy functionality
        li.appendChild(buyBtn);

        cartList.appendChild(li);
    });
}

function removeFromCart(index) {
    const cart = JSON.parse(localStorage.getItem('cart')) || [];
    cart.splice(index, 1);
    localStorage.setItem('cart', JSON.stringify(cart));
    showCart();
}

function buyAll() {
    alert('Implement the "Buy All Now" functionality here!');
    // You can proceed with purchasing all items in the cart
}

showCart();
