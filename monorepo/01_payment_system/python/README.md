# Crear ambiente de desarrollo
## Linux
- `sudo apt-get install python3-venv`    # If needed
- `python3 -m venv .venv`
- `source .venv/bin/activate`

## macOS
- `python3 -m venv .venv`
- `source .venv/bin/activate`

## Windows
- `py -3 -m venv .venv`
- `.venv\scripts\activate`


# Run server
`python manage.py runserver 0.0.0.0:8000`



# Para agregar una libreria común a todos las apps en el proyecto

Para agregar una biblioteca o librería que pueda ser compartida por todas las aplicaciones en el proyecto Django, seguiremos estos pasos:

1. Crearemos la nueva carpeta `libs` en el directorio raíz de tu proyecto Django. 

2. Los archivos comunes a distintas apps deberán estar en esta blioteca asi como archivos de configuración, archivos de plantillas u otros archivos.

3. Para que funcione las llamadas a esta liberia deberemos usar la variable `BASE_DIR` en el archivo `settings.py` de Django como referencia. 

```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LIBRARY_DIR = os.path.join(BASE_DIR, 'libs')
```

`LIBRARY_DIR` representa la ruta completa hacia la carpeta de la biblioteca.

Hemos actualizado la configuración de `sys.path` en el archivo `settings.py` para incluir la ruta de la biblioteca. Agregando la siguiente línea de código al archivo:

```python
import sys

sys.path.append(LIBRARY_DIR)
```

Esto asegura que Django pueda encontrar los archivos de la biblioteca al buscar en el `sys.path`.

Por ejemplo:

```python
from libs.hello_world import hello_world

result = hello_world()
print(result)
```


# Pruebas Unitarias

Para agregar pruebas unitarias al proyecto:

- Crearemos un archivo de pruebas en el directorio de la aplicación Django para las pruebas unitarias. Por convención, utilizaremos el nombre `tests.py`.

- Dentro de la clase de prueba, definimos los métodos de prueba utilizando nombres que comiencen con `test_`. Estos métodos se ejecutarán automáticamente como pruebas unitarias.

- Ejecuta las pruebas utilizando el comando `python manage.py test` en la terminal. 

Ejemplo: 
```python
from django.test import TestCase
from AbarroteDigital.models import Product

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name='Product 1', price=9.99)
        Product.objects.create(name='Product 2', price=19.99)

    def test_product_name(self):
        product = Product.objects.get(name='Product 1')
        self.assertEqual(product.name, 'Product 1')

    def test_product_price(self):
        product = Product.objects.get(name='Product 2')
        self.assertAlmostEqual(product.price, 19.99, places=2)
```

En este ejemplo, se crea una clase de prueba `ProductTestCase` que hereda de `TestCase`. Se define el método `setUp` para configurar los datos de prueba creando objetos `Product`. Luego, se definen dos métodos de prueba: `test_product_name` y `test_product_price`, que realizan aserciones para verificar el nombre y el precio de los productos.

Al ejecutar el comando `python manage.py test`, Django buscará y ejecutará las pruebas definidas en el archivo `tests.py` y mostrará los resultados en la terminal.

# Pruebas Funcionales

Las pruebas funcionales las 

# Pruebas de integración