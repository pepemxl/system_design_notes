# Introducción al diseño y arquitectura de sistemas escalables

El **diseño de sistemas** es un proceso que implica la creación y configuración de sistemas complejos para cumplir con ciertos objetivos y requerimientos. Los sistemas informaticos varian en naturaleza y escala, en estas notas nos enfocaremos en sistemas industriales.

En resumen, el diseño de sistemas es un proceso multidisciplinario que implica la planificación, especificación y configuración de sistemas complejos para cumplir con objetivos específicos en una variedad de campos y aplicaciones. Veremos los casos más comunes en los últimos años.


Un **sistema escalable y centrado en datos**, también conocido como "**data-intensive system**" en inglés, generalmente consta de varios componentes que trabajan juntos para gestionar grandes volúmenes de datos de manera eficiente y escalable. Aquí hay algunos componentes comunes que podrías encontrar en este tipo de sistemas:

1. **Almacenamiento de Datos Distribuido**: Este componente es fundamental en un sistema escalable centrado en datos. Suele consistir en una infraestructura distribuida que permite almacenar grandes cantidades de datos de forma redundante y escalable, como sistemas de archivos distribuidos o bases de datos distribuidas.

2. **Procesamiento Distribuido**: Para manejar grandes volúmenes de datos, es necesario distribuir el procesamiento en múltiples nodos. Esto puede implicar el uso de sistemas de procesamiento distribuido como Apache Hadoop, Apache Spark, o sistemas de procesamiento de flujo como Apache Flink.

3. **Gestión de Datos en Tiempo Real**: En algunos casos, el sistema puede necesitar procesar datos en tiempo real. Esto implica componentes que pueden manejar flujos de datos continuos y tomar decisiones en tiempo real, como sistemas de procesamiento de eventos complejos (CEP, por sus siglas en inglés) o sistemas de streaming.

4. **Capa de Almacenamiento de Datos en Memoria**: Para mejorar el rendimiento y la latencia, muchos sistemas escalables centrados en datos utilizan una capa de almacenamiento en memoria para almacenar datos temporalmente y reducir el acceso a disco. Ejemplos de tecnologías utilizadas incluyen Apache Kafka para la mensajería en memoria o sistemas de caché como Redis o Memcached.

5. **Gestión de Metadatos**: Con grandes volúmenes de datos, es esencial tener una gestión eficiente de los metadatos. Esto puede incluir sistemas de catálogo de datos para organizar y describir los conjuntos de datos disponibles, así como sistemas de metadatos distribuidos para rastrear la ubicación y el estado de los datos almacenados.

6. **Escalabilidad Horizontal**: Los sistemas escalables centrados en datos generalmente se diseñan para escalar horizontalmente, lo que significa que pueden crecer agregando más nodos al sistema en lugar de aumentar los recursos en un solo nodo. Esto requiere diseños de sistemas que sean distribuidos y que puedan manejar la adición de nuevos nodos sin interrupciones en el servicio.


## Pautas para este proyecto

Desarrollaremos las herramientas necesarias para escalar las aplicaciones y reutilizar código escrito en distintos lenguajes de programación, organizar un proyecto que trabaje con varias subaplicaciones y microservicios en diferentes lenguajes de programación puede ser un desafío, pero hay algunas prácticas recomendadas que pueden ayudar a mantener el proyecto organizado y manejable. A continuación, se presentan algunas recomendaciones generales:

1. Seleccionaremos un sistema de gestión de versiones: Es importante seleccionar un sistema de gestión de versiones, en este caso será Git como parte de las mismas notas, con esto nos aseguraremos de que todos los cambios realizados tanto en el proyecto como en la documentación se puedan rastrear y administrar de manera efectiva.

2. Usaremos un sistema de integración continua: Un sistema de integración continua local, como Jenkins o Travis CI, para ayudar a asegurarnos de que todas las subaplicaciones y microservicios estén integrados y funcionen correctamente juntos.

3. Utilizaremos contenedores en docker: El uso de contenedores, como Docker, y una herramienta de orquestación, como Kubernetes(para aquellos proyectos que necesiten ser deployados en cloud) y docker-swarm para desarrollo local, esto nos ayudará a simplificar la gestión de los microservicios en diferentes lenguajes de programación, también haremos algunas prácticas con mesos y zookeper.

4. Definir estándares de código: Tal vez una de las partes más complicadas de definir en un sistema con multiples lenguajes, es importante definir estándares de código para cada uno de los lenguajes de programación utilizados en el proyecto. Esto nos ayudará a garantizar que el código sea legible para todos los involucrados, y facilite las tareas de mantenimiento y coherencia en todas las subaplicaciones.

5. Establecer una arquitectura clara, será nuestro principal objetivo en este proyecto, estableceremos cómo las diferentes subaplicaciones y microservicios se comunicarán entre sí. Esto puede incluir el uso de patrones de diseño como SOAP, RESTful API o Event-Driven Architecture.

6. Separar las responsabilidades: Cada subaplicación y microservicio debe tener una responsabilidad claramente definida. Esto ayudará a garantizar que cada uno esté enfocado en su tarea específica y no se vuelva demasiado complejo.

7. Utilizaremos una herramienta de monitoreo: Para mantener un control efectivo del proyecto y garantizar que todo funcione correctamente, es importante utilizar una herramienta de monitoreo, como Datadog o Prometheus. Aunque para estas tenemos muchas opciones, trataremos de habilitarlas durante las fases de pruebas para este proyecto, idealmente siempre estarian trabajando, lo cual nos permitiria conocer los thresholds y problemas que ocasionan cambios en los distintos sistemas.




Para poder crear aplicaciones lo más realista posible pasaremos algún tiempo seteando servicios gratuitos de sistemas third party comunes en la industria.