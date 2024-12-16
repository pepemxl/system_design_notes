# API Gateway

Un API Gateway o puerta de enlace de API es un componente fundamental en la arquitectura de microservicios que actúa como un punto de entrada unificado para todas las solicitudes dirigidas a un conjunto de servicios backend.

## Caracteristicas Principales


- Encaminamiento de Solicitudes: Dirige las solicitudes entrantes al microservicio adecuado dentro de un sistema distribuido.
- Agregación de Respuestas: Combina respuestas de múltiples servicios backend en una sola respuesta, reduciendo el número de llamadas necesarias desde el cliente.
- Seguridad: Implementa autenticación, autorización y otras políticas de seguridad, protegiendo los servicios backend de accesos no autorizados.
- Control de Tráfico: Administra el tráfico, incluyendo la limitación de tasa, balanceo de carga y manejo de picos de tráfico.
- Conversión de Protocolos: Transforma protocolos de comunicación, por ejemplo, de HTTP a WebSocket, para que los servicios backend no necesiten soportar múltiples protocolos.
- Monitoreo y Registro: Proporciona capacidades de monitoreo, registro de solicitudes y generación de métricas para ayudar en el análisis y la solución de problemas.

- Manipulación de Solicitudes y Respuestas: Realiza tareas de transformación y enriquecimiento de datos, como agregar encabezados o modificar el formato de las respuestas.

## Beneficios de un API Gateway

- Simplificación del Cliente: Los clientes interactúan con un único punto de entrada en lugar de múltiples servicios.
- Seguridad Centralizada: Mejora la seguridad al gestionar la autenticación y autorización en un solo lugar.
- Desempeño Optimizado: Permite la optimización de la comunicación entre el cliente y los servicios backend, reduciendo la latencia y mejorando el rendimiento general.

- Mantenibilidad y Escalabilidad: Facilita la gestión de servicios individuales y la escalabilidad del sistema completo.

## Ejemplos de API Gateways

- **Envoy**: Envoy es un proxy de servicios de código abierto diseñado para facilitar la comunicación y el manejo de tráfico en arquitecturas de microservicios. Fue desarrollado por Lyft y está escrito en C++. Envoy es parte del proyecto CNCF (Cloud Native Computing Foundation) y se utiliza ampliamente para mejorar la observabilidad, seguridad y confiabilidad de las aplicaciones distribuidas.
- **Kong**: Una puerta de enlace de API popular y de código abierto que ofrece características extensibles mediante plugins.
- **Amazon API Gateway**: Un servicio gestionado de AWS que permite a los desarrolladores crear, publicar, mantener, monitorear y asegurar APIs a cualquier escala.
- **Apigee**: Una plataforma de gestión de API de Google Cloud que proporciona herramientas para la creación, el análisis y la monetización de APIs.

