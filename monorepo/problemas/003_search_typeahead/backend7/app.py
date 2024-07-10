from flask import Flask, request, jsonify
import tracemalloc


tracemalloc.start()
app = Flask(__name__)

pre_data = [
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

def augmented_data(pre_data: list, n_samples: int = 100):
    data = []
    pre_data.sort()
    for item in pre_data:
        data.append(item)
        for i in range(n_samples):
            aux = item + "_" + str(i).zfill(4)
            data.append(aux)
    return data


data = augmented_data(pre_data=pre_data, n_samples=1000)


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    suggestions = [item.lower() for item in data if item.lower().startswith(query)]
    return jsonify(suggestions)


@app.route('/memory', methods=['GET'])
def memory():
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    return jsonify({
        "memory_stats": str(top_stats[:10])
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
