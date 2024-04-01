#  Delayed Task Executor

## Descripción

Se requiere diseñar un sistema para ejecutar tareas diferidas con un retraso específico. El sistema debe permitir la programación de múltiples tareas para ejecutarse después de un cierto período de tiempo.

## Requisitos Funcionales

1. **Agregar Tarea Diferida:** El sistema debe permitir a los usuarios agregar tareas con un retraso específico, especificando la función de la tarea y el tiempo de retraso antes de su ejecución.
2. **Ejecutar Tareas Diferidas:** El sistema debe ejecutar las tareas diferidas después de que haya transcurrido el tiempo de retraso especificado para cada tarea.
3. **Múltiples Tareas:** El sistema debe admitir la programación de múltiples tareas diferidas simultáneamente.
4. **Interfaz de Usuario:** El sistema debe proporcionar una interfaz de usuario simple para agregar y administrar tareas diferidas.

## Requisitos No Funcionales

1. **Eficiencia:** El sistema debe ser eficiente en la ejecución de tareas diferidas, minimizando el tiempo de espera entre la programación y la ejecución de las tareas.
2. **Escalabilidad:** El sistema debe ser capaz de manejar un gran número de tareas diferidas sin degradación significativa del rendimiento.
3. **Fiabilidad:** El sistema debe ser robusto y tolerante a fallos, asegurando que todas las tareas diferidas se ejecuten correctamente según lo programado.

## Consideraciones Adicionales

- El sistema debe ser diseñado teniendo en cuenta la **concurrencia** y la **sincronización** para garantizar un comportamiento correcto en entornos **multi-hilo**.

- Se debe proporcionar una solución que minimice la **latencia** y el **consumo de recursos** del sistema.

---

Durante las entrevistas, se espera que se discuta y diseñe una solución que cumpla con estos requisitos, teniendo en cuenta los principios de diseño de sistemas distribuidos.


