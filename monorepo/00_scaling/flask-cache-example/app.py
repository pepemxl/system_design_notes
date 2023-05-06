from flask import Flask
from flask_caching import Cache
import time

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
@cache.cached(timeout=300) # tiempo de caché en segundos
def hello_world():
    time.sleep(100) # simulando una respuesta lenta
    return '¡Hola mundo!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
