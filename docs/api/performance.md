# Performance

Los 5 caminos comunes para mejorar el performance de tu API son:

## Paginación de resultados

Este metodo se utiliza para optimizar resultados grandes usando streaming hacia el cliente, mejorando asi la respuesta y experiencia del usuario.


## Logging Asincrono

Este metodo consiste en enviar logs a un buffer(lock-free). Los logs son periodicamente flusheados a disco, lo cual reduce el overhead de I/O.

## Data Caching

Los datos frrecuentemente accesados son guardados en cache para acelerar el acceso a los datos. El cliente primero revisa en la cache antes de intentar ir a recuperar los datos a la base de datos, usualmente usando bases de datos como Redis.

## Payload Compression

Para reducir el tiempo de transmisión de datos, resquest y respuestas(responses), puede ser compresas acelerando la carga y descarga.

## Connection Pooling

Esta tecnica involucra usar un pool de conecciones abiertas para manejar la interacción con la base de datos, lo cual reduce el overhead de estar abriendo y cerrando conecciones.


