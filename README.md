# Notas de Diseño de Sistemas

En estas notas exploraremos el diseño varios de los sistemas más utilizados en la industria, asi como algunas versiones simples de los mismos que nos permitirán comparar el mismo sistema con diferentes stacks tecnologicos. Además repasaremos algunos de los conceptos básicos del diseño de sistemas.

## Pautas para este proyecto

Desarrollaremos las herramientas necesarias para escalar las aplicaciones y reutilizar código escrito en distintos lenguajes de programación, organizar un proyecto que trabaje con varias subaplicaciones y microservicios en diferentes lenguajes de programación puede ser un desafío, pero hay algunas prácticas recomendadas que pueden ayudar a mantener el proyecto organizado y manejable. A continuación, se presentan algunas recomendaciones generales:

1. Seleccionaremos un sistema de gestión de versiones: Es importante seleccionar un sistema de gestión de versiones, en este caso será Git como parte de las mismas notas, con esto nos aseguraremos de que todos los cambios realizados tanto en el proyecto como en la documentación se puedan rastrear y administrar de manera efectiva.

2. Usaremos un sistema de integración continua: Un sistema de integración continua local, como Jenkins o Travis CI, para ayudar a asegurarnos de que todas las subaplicaciones y microservicios estén integrados y funcionen correctamente juntos.

3. Utilizaremos contenedores en docker: El uso de contenedores, como Docker, y una herramienta de orquestación, como Kubernetes, nos ayudará a simplificar la gestión de los microservicios en diferentes lenguajes de programación, también haremos algunas prácticas en mesos y zookeper.

4. Definir estándares de código: Tal vez una de las partes más complicadas de definir en un sistema con multiples lenguajes, es importante definir estándares de código para cada uno de los lenguajes de programación utilizados en el proyecto. Esto nos ayudará a garantizar que el código sea legible para todos los involucrados, y facilite las tareas de mantenimiento y coherencia en todas las subaplicaciones.

5. Establecer una arquitectura clara, será nuestro principal objetivo en este proyecto, estableceremos cómo las diferentes subaplicaciones y microservicios se comunicarán entre sí. Esto puede incluir el uso de patrones de diseño como SOAP, RESTful API o Event-Driven Architecture.

6. Separar las responsabilidades: Cada subaplicación y microservicio debe tener una responsabilidad claramente definida. Esto ayudará a garantizar que cada uno esté enfocado en su tarea específica y no se vuelva demasiado complejo.

7. Utilizaremos una herramienta de monitoreo: Para mantener un control efectivo del proyecto y garantizar que todo funcione correctamente, es importante utilizar una herramienta de monitoreo, como Datadog o Prometheus. Aunque para estas tenemos muchas opciones, trataremos de habilitarlas durante las fases de pruebas para este proyecto, idealmente siempre estarian trabajando, lo cual nos permitiria conocer los thresholds y problemas que ocasionan cambios en los distintos sistemas.

### Algunas herramientas de monitoreo
- Splunk: Es una herramienta de análisis de datos que permite a las empresas recopilar y analizar grandes cantidades de datos de múltiples fuentes para obtener información en tiempo real.

- Datadog: Es una plataforma de monitoreo y análisis de logs en tiempo real que ayuda a los equipos de operaciones a rastrear el rendimiento de sus aplicaciones y servicios.

- Grafana: Es una plataforma de análisis y monitoreo que se integra con múltiples fuentes de datos para proporcionar una visualización en tiempo real de los datos.

- Nagios: Es una herramienta de monitoreo de código abierto que permite monitorear la disponibilidad y la salud de los servidores, redes y aplicaciones.

- Zabbix: Es una solución de monitoreo de red y aplicaciones de código abierto que permite recopilar datos de diferentes fuentes, como dispositivos de red, servidores, aplicaciones y servicios.

- Prometheus: Es una solución de monitoreo de código abierto que se especializa en monitorear aplicaciones y servicios en contenedores.

- New Relic: Es una plataforma de monitoreo de aplicaciones en la nube que ayuda a los equipos de desarrollo y operaciones a identificar problemas en las aplicaciones y servicios.


Para poder crear aplicaciones lo más realista posible pasaremos algún tiempo seteando servicios gratuitos de sistemas third party comunes en la industria.


1. ESCALAR UN SISTEMA
    1. [Como escalar de cero a millones de usuarios.](documentation/como_escalar_de_cero_a_millones_de_usuarios/01_section_escalamiento.md)
    2. [Estimando sobre la marcha.](documentation/como_escalar_de_cero_a_millones_de_usuarios/02_section_estimacion.md)
2. DISEÑO DE UN SISTEMA DE PAGOS
3. DISEÑO DE UN ACORTADOR DE URL
4. DISEÑO DE UN SISTEMA DE NOTIFICACIONES
5. DISEÑO DE UN SISTEMA DE DONACIONES
6. DISEÑO DE UN SISTEMA NEWS FEED
7. DISEÑO DE UN LIMITADOR DE TARIFAS (RATE LIMITER)
8. DISEÑO DE HASHING CONSISTENTE
9. DISEÑO DE UNA ALMACEN DE CLAVES-VALOR
10. DISEÑO DE UN GENERADOR DE IDENTIFICADORES ÚNICOS EN SISTEMAS DISTRIBUIDOS
11. DISEÑO DE UN WEB-CRAWLER
12. DISEÑO DE UN SISTEMA DE CHAT
13. DISEÑO DE UN SISTEMA DE AUTOCOMPLETADO DE BÚSQUEDAS
14. DISEÑO DE YOUTUBE
15. DISEÑO DE GOOGLE DRIVE




