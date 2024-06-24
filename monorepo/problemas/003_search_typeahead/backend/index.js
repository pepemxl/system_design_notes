const express = require('express');
const app = express();
const port = 3000;

/*const data = [
    'apple', 'banana', 'grape', 'orange', 'pineapple', 'strawberry', 'watermelon'
];*/

const data = [
    "Manzana", "Banana", "Uva", "Naranja", "Piña", "Fresa", "Sandía", "Melón", 
    "Pera", "Kiwi", "Mango", "Durazno", "Cereza", "Limón", "Lima", "Papaya", 
    "Frambuesa", "Mora", "Arándano", "Granada", "Higo", "Mandarina", "Nectarina", 
    "Guayaba", "Maracuyá", "Coco", "Chirimoya", "Carambola", "Dátil", "Ciruela", 
    "Toronja", "Albaricoque", "Lichi", "Plátano", "Pomelo", "Caqui", "Rambután", 
    "Guanábana", "Pitahaya", "Mangostán", "Noni", "Durian", "Jaca", "Acerola", 
    "Mora azul", "Papaya", "Níspero", "Tamarindo", "Kaki", "Yuzu", "Espárrago", 
    "Brócoli", "Coliflor", "Espinaca", "Kale", "Acelga", "Lechuga", "Rúcula", 
    "Berro", "Col rizada", "Zanahoria", "Pepino", "Pimiento", "Calabacín", 
    "Berenjena", "Tomate", "Cebolla", "Ajo", "Apio", "Puerro", "Alcachofa", 
    "Nabos", "Remolacha", "Rábano", "Col de Bruselas", "Repollo", "Hinojo", 
    "Guisantes", "Judías verdes", "Maíz", "Patata", "Boniato", "Calabaza", 
    "Chayote", "Okra", "Cebolleta", "Acelga", "Endivia", "Escarola", "Mostaza", 
    "Diente de león", "Col china", "Setas", "Champiñón", "Alcachofa de Jerusalén", 
    "Batata", "Jícama", "Chícharos", "Albahaca", "Cilantro"
];



app.get('/search', (req, res) => {
    const query = req.query.q.toLowerCase();
    const suggestions = data.filter(item => item.toLowerCase().startsWith(query));
    res.json(suggestions);
});

app.listen(port, () => {
    console.log(`Servidor ejecutándose en http://localhost:${port}`);
});
