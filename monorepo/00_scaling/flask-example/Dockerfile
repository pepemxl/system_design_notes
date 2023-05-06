FROM python:3.9-slim-buster

WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt requirements.txt

# Instala los paquetes necesarios
RUN pip install -r requirements.txt

# Copia los archivos de la aplicación al contenedor
COPY . .

# Expone el puerto 5000 para acceder a la aplicación
EXPOSE 5001

# Ejecuta la aplicación Flask
CMD ["python", "app.py"]
