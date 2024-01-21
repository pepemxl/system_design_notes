#import unittest
#from flask import Flask
#from flask_cors import CORS
import requests

URL1 = 'http://localhost:5001/cache'
URL2 = 'http://localhost:5002/cache'
URL3 = 'http://localhost:5003/cache'

URL1_store = 'http://localhost:5001/store'
URL2_store = 'http://localhost:5002/store'
URL3_store = 'http://localhost:5003/store'


URL1_store_get = 'http://localhost:5001/store_get'
URL2_store_get = 'http://localhost:5002/store_get'
URL3_store_get = 'http://localhost:5003/store_get'


#class FlaskCacheUnitTest(unittest.TestCase):
    
#    def setUp(self):
#        self.app = Flask(__name__)



def test1():
    response = requests.post(URL1, json={'key':'pepe_key', 'value':'test pepe value'})
    print(response.status_code)
    print(response.json())
    response = requests.get(URL1_store_get)
    print(response.json())
    
def test2():
    response = requests.post(URL2, json={'key':'pepe_key', 'value':'test pepe value'})
    print(response.status_code)
    print(response.json())
    response = requests.get(URL2_store)
    print(response.json())

def test3():
    response = requests.post(URL1, json={'key':'neto_key', 'value':'test neto value'})
    print(response.status_code)
    print(response.json())
    response = requests.get(URL1_store_get)
    print(response.json())

if __name__=='__main__':
    test3()
    #test2()