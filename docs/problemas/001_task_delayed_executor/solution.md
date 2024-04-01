# Solución

Usualmente durante la entevistas no se espera que se codifique toda la solución, si no que se haga utilización de alguna interface, y se expansa su funcionalidad, en este caso atendiendo los requerimientos que podrían o no ser mencionados durante la descripción del problema.

En este caso sabemos que tenemos todos si contados con:

- Requerimientos Funcionales
- Requerimientos No Funcionales
- Consideraciones intrinsecas de cada problema o solución propuesta


Por ejemplo pensando que tenemos la interface para un  ejecutor de tareas

```python
class TaskExecutor:
    def __init__(self):
        self.tasks 

    def add_task(self, task, delay):
        self.tasks.append((task, delay))

    def execute_tasks(self):
        for task, delay in self.tasks:
            time.sleep(delay)
            task()
```


```python
import time
from threading import Thread

class DelayedTaskExecutor:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, delay):
        self.tasks.append((task, delay))

    def execute_tasks(self):
        for task, delay in self.tasks:
            time.sleep(delay)
            task()

def example_task():
    print("Executing a delayed task!")

def main():
    executor = DelayedTaskExecutor()

    # Agregar tareas con un retardo especificado (en segundos)
    executor.add_task(example_task, 3)
    executor.add_task(example_task, 5)

    print("Starting delayed task execution...")

    # Ejecutar tareas en un hilo separado para no bloquear la interfaz de usuario
    task_thread = Thread(target=executor.execute_tasks)
    task_thread.start()

    print("Main program continues while tasks are being executed...")

    # Esperar a que todas las tareas se completen antes de salir
    task_thread.join()

    print("All tasks have been executed.")

if __name__ == "__main__":
    main()

```