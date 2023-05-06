# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:42:52 2023

@author: pepem
"""
import time
import threading
import requests

# Define las URLs a la que enviar las solicitudes
urls = ['http://localhost:5000/',
        'http://localhost:5001/']

# Define el número de solicitudes a enviar
num_requests = 100



# Define una función para enviar las solicitudes
def send_request(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('Error', response.status_code)


def test_urls(urls):
    for url in urls:
        # Mide el tiempo de inicio de las solicitudes
        start_time = time.time()
        
        # Crea una lista de subprocesos para enviar las solicitudes en paralelo
        threads = []
        for i in range(num_requests):
            t = threading.Thread(target=send_request, args=(url,))
            threads.append(t)
        
        # Inicia los subprocesos
        for t in threads:
            t.start()
        
        # Espera a que los subprocesos terminen
        for t in threads:
            t.join()
        
        # Calcula el tiempo total de las solicitudes
        total_time = time.time() - start_time
        
        # Muestra los resultados
        print(f'Test on url: {url}')
        print(f'Total time: {total_time} seconds')
        print(f'Requests per second: {num_requests / total_time}')


if __name__=='__main__':
    test_urls(urls)