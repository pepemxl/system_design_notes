# Performance


Performance es un tema complicado en sistemas escalados, mientras la tendencia es aumentar la velocidad de desarrollo, creando sistemas que puedan interactuar más facilmente, las abstracciones que se requieren para dicha tarea dañan el performance de las aplicaciones. Usualmente durante la etapa de crecimiento es preferido sobre el performance, sin embargo para cuando se quiere realizar optiomizaciones el código ya esta en una fase donde es complicado evaluarlo o modificarlo.


Una estrategia tipica es tratar de actualizar las librerias.

## Upgrade Python

Vamos a testear un simple código donde se ha activado `tracemalloc` para los servicios donde el backend es en python y uno en node que nos servira de referencia, usando un problema sencillo llamado `search typeahead`.


Average latency for service node: 0.1643 seconds
Total time for 100 requests on service node: 0.2373 seconds
Average latency for service flask_python_3.6: 3.0906 seconds
Total time for 100 requests on service flask_python_3.6: 4.1261 seconds
Average latency for service flask_python_3.7: 2.2439 seconds
Total time for 100 requests on service flask_python_3.7: 3.9426 seconds
Average latency for service flask_python_3.8: 3.1209 seconds
Total time for 100 requests on service flask_python_3.8: 5.0944 seconds
Average latency for service flask_python_3.9: 3.7367 seconds
Total time for 100 requests on service flask_python_3.9: 6.9786 seconds
Average latency for service flask_python_3.10: 3.8180 seconds
Total time for 100 requests on service flask_python_3.10: 6.5754 seconds
Average latency for service flask_python_3.11: 4.5415 seconds
Total time for 100 requests on service flask_python_3.11: 8.3956 seconds
Average latency for service flask_python_3.12: 5.0229 seconds
Total time for 100 requests on service flask_python_3.12: 9.4313 seconds
Average latency for service flask_trie_python_3.9: 68.1613 seconds
Total time for 100 requests on service flask_trie_python_3.9: 98.6029 seconds
