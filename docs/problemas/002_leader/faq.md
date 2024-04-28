# FAQ

## 1. Es necesario actualizar en tiempo real?

Usualmente este tipo de preguntas se responde que no es necesario iniciar con esta asumsion sin embargo más adelante se le pide al usuario considerar este caso.

## 2. Cuales son las dimensiones y la cardinalidad de cada dimensión?

| Dimension | Cardinalidad | Número de valores a los que puede pertenecer cada usuario |
| --------- | ------------ | ---------------------------------------------------------- |
| Categorias | 10000 | 10 |
| Areas Metropolitanas | 10000 | 1 |
| Buckets de edad | 6 | 1 |


## 3. Para determinar el rank de un usuario en alguna categoria, contamos el numero de likes?

Si

## 4. Pueden agregarse más dimensiones después?

Si

## 5. Cual es el formato y/o el origen de la data?

Usualmente se le deja al entrevistado elegir como la información esta estructurada y como
es accesada esta información.




## Consideraciones generales cuando hacemos problemas de arquitectura para un rank.

 El desafío radica en diseñar un sistema que sea preciso, escalable y justo. Algunos de los aspectos clave que deben abordarse incluyen:

1. **Algoritmo de clasificación**: Se necesita un algoritmo eficiente y preciso para calcular el ranking de los usuarios en función de la relevancia y la influencia de sus publicaciones. Esto puede incluir factores como la cantidad de interacciones (likes, comentarios, compartidos), la calidad del contenido, la frecuencia de publicación y la retroalimentación de la comunidad.

2. **Escalabilidad**: El sistema debe ser capaz de manejar grandes volúmenes de usuarios y publicaciones sin comprometer el rendimiento. Esto implica diseñar una arquitectura escalable que pueda manejar el aumento en el número de usuarios y datos sin problemas.

3. **Equidad y transparencia**: Es crucial garantizar que el sistema de clasificación sea justo y transparente para todos los usuarios. Esto implica evitar sesgos injustos y proporcionar una explicación clara sobre cómo se calcula el ranking de cada usuario.

4. **Actualización en tiempo real**: El sistema debe ser capaz de actualizar los rankings de los usuarios en tiempo real para reflejar cambios recientes en sus actividades y el comportamiento de la comunidad.

5. **Privacidad y seguridad**: Se deben implementar medidas sólidas para proteger la privacidad de los usuarios y prevenir el abuso del sistema, como el spam o la manipulación de clasificaciones.

6. **Interfaz de usuario intuitiva**: El sistema debe integrarse de manera fluida en la interfaz de usuario existente, proporcionando a los usuarios una forma intuitiva de acceder a su ranking y comprender su posición en la comunidad.

El diseño de este sistema requiere una cuidadosa consideración de estos aspectos para garantizar una experiencia de usuario satisfactoria y promover la participación activa dentro de la plataforma.