# Map Reduce Ejemplo/TASK

Un ejemplo simple de una operación MapReduce en Python para contar la cantidad de palabras en un conjunto de documentos. Crearemos una función mapper que toma un documento como entrada y emite pares clave-valor donde la clave es una palabra y el valor es 1, y una función reducer que suma los valores asociados con cada clave para obtener el recuento total de palabras.

Compararemos los tiempos de ejecucion.


- Crear 10 millon de lineas de texto de a los más 80 caracteres(documentos)
- Calcular cuantas veces aparece cada palabra en este millon de lineas de texto
- Usar map reduce.


Disponemos de:

- Una maquina con 10 cores.
- Usaremos flask para hacer el servicio al cual le mandremos las lineas de texto
- Crear 5 instancias de docker cada una usando 2 cores y a lo más un 1GB de ram.

Vamos a medir el performance de nuestra aplicación.

- Monitorear la memoria de nuestra aplicación
- Monitorear la memoria del contenedor de docker
- Monitorear la CPU usada por nuestra aplicación
- Monitorear la CPU usada por nuestro contenedor de docker


