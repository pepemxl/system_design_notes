from flask import Flask, request, jsonify
import os
import redis


app = Flask(__name__)
# Configurar conexión a Redis
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

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

# Inicializar Redis con los datos desde el arreglo data
# tenemos dos keys data_initialized que guarda el status y data que guarda la lista de datos
def initialize_redis(data=data):
    if not r.exists('data_initialized'):
        for word in data:
            item = word.strip()
            r.sadd('data', item)
        r.set('data_initialized', '1')

initialize_redis()


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    suggestions = [item for item in r.smembers('data') if item.lower().startswith(query)]
    return jsonify(suggestions)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
