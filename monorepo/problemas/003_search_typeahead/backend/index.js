const express = require('express');
const app = express();
const port = 5000;


const preData = [
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

function augmentedData(n = 100, preData = []) {
    let data = [];
    preData.sort();
    preData.forEach(item => {
        for (let i = 0; i < n; i++) {
            let aux = item + "_" + String(i).padStart(4, '0');
            data.push(aux);
        }
    });
    return data;
};

const data = augmentedData(100, preData);


app.get('/search', (req, res) => {
    const query = req.query.q.toLowerCase();
    const suggestions = data.filter(item => item.toLowerCase().startsWith(query));
    res.json(suggestions);
});

app.listen(port, () => {
    console.log(`Servidor ejecutándose en http://localhost:${port}`);
});
