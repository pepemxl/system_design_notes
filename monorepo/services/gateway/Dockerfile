# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Exponer el puerto que la aplicación usa
EXPOSE 5000

# Define el comando para ejecutar la aplicación
CMD ["python", "gateway.py"]
