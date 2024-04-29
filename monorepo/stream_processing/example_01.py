"""
Este ejemplo asume que tienes una función mapper que toma un documento como entrada y emite pares clave-valor donde la clave es una palabra y el valor es 1, 
y una función reducer que suma los valores asociados con cada clave para obtener el recuento total de palabras.
"""
from collections import defaultdict

# Función Mapper
def mapper(document):
    word_count = defaultdict(int)
    for word in document.split():
        word_count[word] += 1
    for word, count in word_count.items():
        yield (word, count)

# Función Reducer
def reducer(word, counts):
    yield (word, sum(counts))

# Datos de entrada (documentos)
documents = [
    "el gato está en la casa",
    "el perro está en el jardín",
    "el pájaro está en el árbol"
]

# Fase Map
mapped_data = []
for document in documents:
    mapped_data.extend(mapper(document))

# Shuffle and Sort (opcional en este caso)

# Fase Reduce
word_counts = defaultdict(list)
for word, count in mapped_data:
    word_counts[word].append(count)

# Resultados finales
final_result = {}
for word, counts in word_counts.items():
    final_result[word] = sum(counts)

# Mostrar los resultados
for word, count in final_result.items():
    print(f"{word}: {count}")
