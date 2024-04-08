function agregarProducto(producto) {
    let carrito = localStorage.getItem('carrito');
    if (!carrito) {
        carrito = [];
    } else {
        carrito = JSON.parse(carrito);
    }
    let productoEncontrado = carrito.find(p => p.id === producto.id);
    if (productoEncontrado) {
        productoEncontrado.cantidad++;
        console.log('Producto encontrado');
        console.log(carrito);
    } else {
        let nuevoProducto = producto;
        nuevoProducto.cantidad = 1;
        carrito.push(nuevoProducto);
        console.log('Producto no encontrado, añadido al carrito');
        console.log(carrito);
    }
    localStorage.setItem('carrito', JSON.stringify(carrito));
}

function actualizarCuentaCarrito(){
    let carrito = JSON.parse(localStorage.getItem('carrito'));
    let total = carrito.reduce((acc, p) => acc + p.cantidad, 0);
    document.getElementById("cuenta-carrito").innerText = total;
}

actualizarCuentaCarrito();
