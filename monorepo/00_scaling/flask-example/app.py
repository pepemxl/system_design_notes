from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    time.sleep(100) # simulando una respuesta lenta de un 1s
    return '¡Hola mundo!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
