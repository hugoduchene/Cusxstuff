class StorageHandler {
    constructor(variableStorageName = null) {
      this.cart = [];
      // Génère un nom de variable aléatoire pour le localStorage
      this.storageVariable =
        variableStorageName ?? `${new Date().getTime()}-storage`;
    }
  
    getContent() {
      return JSON.parse(localStorage.getItem(this.storageVariable));
    }
  
    setContent(cartContent) {
      this.cart = cartContent ?? [];
      window.localStorage.setItem(
        this.storageVariable,
        JSON.stringify(this.cart)
      );
    }
  }
  
  // Déclaration et instanciation
  const shoppingCart = new StorageHandler();
  // Variable qui contient le panier
  const myShopping = [
    {
      name: "Croquette pour chat",
      quantity: 10,
      price: 10.1
    },
    {
      name: "Croquette pour chien",
      quantity: 20,
      price: 30.1
    }
  ];
  
  // Sauvegarde des données dans le localStorage
  shoppingCart.setContent(myShopping);
  
  // Obtention des données depuis le localStorage
  console.table(shoppingCart.getContent())