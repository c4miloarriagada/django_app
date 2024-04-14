document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("form");
  
    form.addEventListener("submit", function (event) {
      event.preventDefault();
  
      const passwordInput = document.getElementById("password");
      const password = passwordInput.value;
  
      // Validación de minimo y margen de caracteres
      if (password.length < 8) {
        alert("La contraseña debe tener minimo 8.");
        return;
      }
  
      // Validación de letras y números
      const containsLetters = /[a-zA-Z]/.test(password);
      const containsNumbers = /[0-9]/.test(password);
      if (!containsLetters || !containsNumbers) {
        alert("La contraseña debe contener tanto letras como números.");
        return;
      }
  
      form.submit();
    });
  });