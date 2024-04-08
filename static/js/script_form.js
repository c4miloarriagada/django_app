const form = document.querySelector('#form')

document.addEventListener('DOMContentLoaded', function() {
  const form = document.querySelector('#form');
  const limpiarBoton = document.getElementById('limpiarFormulario');

  limpiarBoton.addEventListener('click', function() {
    form.reset();
  });
});

form.addEventListener('submit', (event) => {
  event.preventDefault()
  const formData = new FormData(form)
  const nombre = formData.get('nombre')
  const email = formData.get('email')
  const telefono = formData.get('telefono')
  const password = formData.get('password')
  const confirmPassword = formData.get('confirm-password')
  const address = formData.get('address')
  const fechaNacimiento = formData.get('fecha_nacimiento')

  if (
    !validateEMail(email) ||
    !validateNumero(telefono) ||
    !validateName(nombre) ||
    !validatePassword(password, confirmPassword) ||
    !validatePassword(address) ||
    !validatePassword(fechaNacimiento)
  ) {
    form.classList.add('error')
    return
  }

  form.classList.remove('error')
  simularAsync(formData)
    .then((data) => data)
    .catch((err) => console.error(err))
})

const simularAsync = (form) => {
  return fetch('/some-url', {
    method: 'POST',
    body: JSON.stringify(form)
  })
    .then((res) => res.json())
    .catch((err) => console.warn(err))
}

const validateEMail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/

  return emailRegex.test(email)
}

const validateName = (nombre) => {
  return nombre.trim().length > 5
}

const validateNumero = (numero) => {
  const phoneRegex = /^569\d{8}$/

  return phoneRegex.test(numero)
}

const validatePassword = (password, confirmPassword) => {
  if (password !== confirmPassword) {
    return false;
  }

const numberRegex = /\d/;
  const uppercaseRegex = /[A-Z]/;
  if (!numberRegex.test(password) || !uppercaseRegex.test(password)) {
    return false;
  }
  return true;
}

const validateAge = (fechaNacimiento) => {
  const today = new Date();
  const birthday = new Date(fechaNacimiento);
  const age = today.getFullYear() - birthday.getFullYear();
  return age >= 13;
}


