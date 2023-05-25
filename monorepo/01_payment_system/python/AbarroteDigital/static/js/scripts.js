// scripts.js

// Función para mostrar un mensaje al hacer clic en un producto
function showMessage(productName) {
    alert("Has seleccionado el producto: " + productName);
  }
  
  // Asignar el evento clic a todos los productos
  var productCards = document.querySelectorAll(".product-card");
  productCards.forEach(function (card) {
    card.addEventListener("click", function () {
      var productName = this.querySelector(".product-name").textContent;
      showMessage(productName);
    });
  });
  