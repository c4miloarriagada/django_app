const juegoscontainer = document.getElementById("juegos-container");

function crearTarjetaJuego(juegos) {
  juegos.forEach((juego) => {
    if (juego.categoria !== "Accion") {
      return;
    }
    const nuevojuego = document.createElement("div");
    nuevojuego.classList.add("juego");
    nuevojuego.innerHTML = `	
        <img src="${juego.Image}" alt="${juego.nombre}" />
        <h3>${juego.nombre}</h3>
        <p>${juego.precio}</p>
        <button>Agregar al carrito</button>
        `;
    juegoscontainer.appendChild(nuevojuego);
    nuevojuego.getElementsByTagName("button")[0].addEventListener("click", () => {
      agregarProducto(juego);
      Toastify({
        text: "Añadido al carrito",
        duration: 3000,
        destination: "../carrito/index.html",
        newWindow: true,
        close: true,
        gravity: "bottom", // `top` or `bottom`
        position: "right", // `left`, `center` or `right`
        stopOnFocus: true, 
        style: {
          background: "linear-gradient(to right, #ff9900, #212529)",
          
        }
      }).showToast();
      actualizarCuentaCarrito();
    });
  });
}

crearTarjetaJuego(juegos);