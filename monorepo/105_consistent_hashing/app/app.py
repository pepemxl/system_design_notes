# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import hashlib

# Creamos N instancias de flask
app1 = Flask(__name__)
cors1 = CORS(app1, resources={r"/*": {"origins": "*"}})
app2 = Flask(__name__)
cors2 = CORS(app2, resources={r"/*": {"origins": "*"}})
app3 = Flask(__name__)
cors3 = CORS(app3, resources={r"/*": {"origins": "*"}})

cache = {}


@app1.route('/cache', methods=['POST'])
def cache1():
    data = request.get_json()
    key = data['key']
    value = data['value']
    server_id = int(hashlib.sha256(key.encode()).hexdigest(), 16)%3
    print("Server ID: {0}".format(server_id))
    if server_id == 0:
        response = requests.post('http://localhost:5001/store', json={'key':key, 'value':value})
    elif server_id == 1:
        response = requests.post('http://localhost:5002/store', json={'key':key, 'value':value})
    elif server_id == 2:
        response = requests.post('http://localhost:5003/store', json={'key':key, 'value':value})
    return jsonify({'result': 'success', 'server_id': server_id})


@app1.route('/store', methods = ['POST'])
def store1():
    data = request.get_json()
    key = data['key']
    value = data['value']
    cache[key] = value
    return jsonify({'result': 'success', 'store':1})

@app1.route('/store_get', methods = ['GET'])
def store_get():
    try:
        data = cache.copy()
        return jsonify({'result': 'success', 'store':1, 'data':data})
    except:
        return jsonify({'result': 'error'})

@app2.route('/cache', methods=['POST'])
def cache2():
    data = request.get_json()
    key = data['key']
    value = data['value']
    server_id = int(hashlib.sha256(key.encode()).hexdigest(), 16)%3
    if server_id == 0:
        response = requests.post('http://localhost:5001/store', json={'key':key, 'value':value})
    elif server_id == 1:
        response = requests.post('http://localhost:5002/store', json={'key':key, 'value':value})
    elif server_id == 2:
        response = requests.post('http://localhost:5003/store', json={'key':key, 'value':value})
    return jsonify({'result': 'success'})


@app2.route('/store', methods = ['POST'])
def store2():
    data = request.get_json()
    key = data['key']
    value = data['value']
    cache[key] = value
    return jsonify({'result': 'success', 'store':2})

@app2.route('/store_get', methods = ['GET'])
def store_get():
    data = cache.copy()
    return jsonify({'result': 'success', 'store':2, 'data':data})

@app3.route('/cache', methods=['POST'])
def cache3():
    data = request.get_json()
    key = data['key']
    value = data['value']
    server_id = int(hashlib.sha256(key.encode()).hexdigest(), 16)%3
    if server_id == 0:
        response = requests.post('http://localhost:5001/store', json={'key':key, 'value':value})
    elif server_id == 1:
        response = requests.post('http://localhost:5002/store', json={'key':key, 'value':value})
    elif server_id == 2:
        response = requests.post('http://localhost:5003/store', json={'key':key, 'value':value})
    return jsonify({'result': 'success'})


@app3.route('/store', methods = ['POST'])
def store3():
    data = request.get_json()
    key = data['key']
    value = data['value']
    cache[key] = value
    return jsonify({'result': 'success', 'store':3})

@app3.route('/store_get', methods = ['GET'])
def store_get():
    data = cache.copy()
    return jsonify({'result': 'success', 'store':3, 'data':data})

if __name__=='__main__':
    app1.run(debug=True, host='localhost', port=5001)
    app2.run(debug=True, host='localhost', port=5002)
    app3.run(debug=True, host='localhost', port=5003)