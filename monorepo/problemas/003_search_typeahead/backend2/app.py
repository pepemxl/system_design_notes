from flask import Flask, request, jsonify
import time

app = Flask(__name__)

data = [
    "Manzana", "Banana", "Uva", "Naranja", "Piña", "Fresa", "Sandía", "Melón", 
    "Pera", "Kiwi", "Mango", "Durazno", "Cereza", "Limón", "Lima", "Papaya", 
    "Frambuesa", "Mora", "Arándano", "Granada", "Higo", "Mandarina", "Nectarina", 
    "Guayaba", "Maracuyá", "Coco", "Chirimoya", "Carambola", "Dátil", "Ciruela", 
    "Toronja", "Albaricoque", "Lichi", "Plátano", "Pomelo", "Caqui", "Rambután", 
    "Guanábana", "Pitahaya", "Mangostán", "Noni", "Durian", "Jaca", "Acerola", 
    "Mora azul", "Níspero", "Tamarindo", "Kaki", "Yuzu", "Espárrago", 
    "Brócoli", "Coliflor", "Espinaca", "Kale", "Acelga", "Lechuga", "Rúcula", 
    "Berro", "Col rizada", "Zanahoria", "Pepino", "Pimiento", "Calabacín", 
    "Berenjena", "Tomate", "Cebolla", "Ajo", "Apio", "Puerro", "Alcachofa", 
    "Nabos", "Remolacha", "Rábano", "Col de Bruselas", "Repollo", "Hinojo", 
    "Guisantes", "Judías verdes", "Maíz", "Patata", "Boniato", "Calabaza", 
    "Chayote", "Okra", "Cebolleta", "Acelga", "Endivia", "Escarola", "Mostaza", 
    "Diente de león", "Col china", "Setas", "Champiñón", "Alcachofa de Jerusalén", 
    "Batata", "Jícama", "Chícharos", "Albahaca", "Cilantro" 
]

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    suggestions = [item.lower() for item in data if item.lower().startswith(query)]
    # time.sleep(1)
    return jsonify(suggestions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
