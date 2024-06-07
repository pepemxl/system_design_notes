# Solución

1. Logs serán enviadas a kafka(o similar queue log message)
2. Un broker de kafka va a despachar los mensajes a los consumidores, usualmente persistiremos esto en S3 por un periodo de tiempo prefijado (horas/dias).
3. Creamos una tabla ya sea en hive o iceberg para guardar la metadata del esquema de la data.
4. Creamos tareas ETL o ELT (jobs) usando herramientas como airflow para correr tareas programadas en Presto/SparkSQL/Spark.
5. En demanda(Ad-Hoc) analisis puede ser realizado con Presto/SparkSQL
6. Calculemos el QPS aproximado basandonos en el tamaño de la data y cuanta información necesitamos persistir en S3
7. Ahora veamos soluciones para los requerimientos de actualización(refresh) y latencia.



- ~250TB exactamente 210TB
- Como escalamos kafka para manejar el QPS