from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ruta para redirigir solicitudes a un servicio backend específico
@app.route('/service1/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def service1(path):
    url = f'http://localhost:5001/{path}'  # URL del servicio backend 1
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    return (response.content, response.status_code, response.headers.items())


@app.route('/service2/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def service2(path):
    url = f'http://localhost:5002/{path}'  # URL del servicio backend 2
    response = requests.request(
        method=request.method,
        url=url,
        headers=request.headers,
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)
    return (response.content, response.status_code, response.headers.items())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
