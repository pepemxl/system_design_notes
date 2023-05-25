# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate

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
from AbarroteDigital.libs.hello_world import hello_world

result = my_function()
print(result)
```
