const juegoscontainer = document.getElementById("juegos-container");

function crearTarjetaJuego() {
  const juegos = JSON.parse(localStorage.getItem("carrito"));
  console.log(juegos);
  if (juegos && juegos.length > 0) {
    juegos.forEach((juego) => {
      const card = document.createElement("div");
      card.classList.add("juego");
      card.innerHTML = `	
            <img src="${juego.Image}" alt="${juego.nombre}" />
            <h3>${juego.nombre}</h3>
            <p>${juego.categoria}</p>
            <span>Cantidad:${juego.cantidad}</span>
            <p>Total: ${juego.precio * juego.cantidad}</p>
            <button><img src = "../../static/trash-svgrepo-com.svg"></button>
            `;
      juegoscontainer.appendChild(card);
      card.getElementsByTagName("button")[0].addEventListener("click", () => {
        eliminarProducto(juego);
        Toastify({
          text: "Eliminado del carrito",
          duration: 3000,
          destination: "../carrito/index.html",
          newWindow: true,
          close: true,
          gravity: "bottom",
          position: "right",
          stopOnFocus: true,
          style: {
            background: "linear-gradient(to right, #ff9900, #212529)",
          },
        }).showToast();
        actualizarCuentaCarrito();
      });
    });
  }
}

function eliminarProducto(juego) {
  let juegos = JSON.parse(localStorage.getItem("carrito"));
    juegos = juegos.filter((j) => j.nombre !== juego.nombre);
    localStorage.setItem("carrito", JSON.stringify(juegos));
    location.reload();

}


crearTarjetaJuego();
