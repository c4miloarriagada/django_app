document.getElementById('agregar').addEventListener('click', agregarProducto);

function agregarProducto(){
        let nombre = document.getElementById('nombre').value;
        let precio = document.getElementById('precio').value;
        let imagen = document.getElementById('imagen').value;
        let categoria = document.getElementById('categoria').value;
        
        let producto = {
                nombre: nombre,
                precio: precio,
                categoria: categoria,
                Image: imagen

        }

        let productoEncontrado = juegos.find(p => p.nombre === producto.nombre);
        if (productoEncontrado) {
                Toastify({
                        text: "Ya se encuentra registrado",
                        duration: 3000,
                        newWindow: true,
                        close: true,
                        gravity: "bottom", 
                        position: "right", 
                        stopOnFocus: true, 
                        style: {
                            background: "linear-gradient(to right, #ff9900, #212529)",
                            
                        }
                    }).showToast();
        } else {
                let ultimoID = juegos[juegos.length - 1].id;
                producto.id = ultimoID + 1;
                juegos.push(producto);
                Toastify({
                        text: "Se ha registrado el producto correctamente",
                        duration: 3000,
                        newWindow: true,
                        close: true,
                        gravity: "bottom", 
                        position: "right", 
                        stopOnFocus: true, 
                        style: {
                            background: "linear-gradient(to right, #ff9900, #212529)",
                            
                        }
                    }).showToast();


        }
}


/*Se intento pero no se pueden agregar archivos por seguridad de los navegadores (segun San Google)*/
/* Se termina una vez empecemos a trabajar con bdd */