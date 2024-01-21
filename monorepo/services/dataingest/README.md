# Proyecto Base Datos Llave Valor


Para empezar a trabajar hemos creado un proyecto de django corriendo la instrucción:

`docker-compose run django django-admin startproject dataingest .`

Una vez creado abrimos el proyecto de django `dataingest/settings.py` y agregamos las siguientes líneas después de `import os`


Django App es la aplicación local de Django que esatará enviando los "datos" es decir será nuestro "Kafka Producer". 

```mermaid
graph LR
    subgraph "Local Machine"
        B(Kafka Producer)
    end
    style B fill:#999944,stroke:#333,stroke-width:2px
```

Por el momento funcionará como una aplicación externa, sin embargo eventualmente se convertirá en un sidecar de cada una de nuestras aplicaciones.


```mermaid
graph LR
    subgraph "Local Machines"
        A(Django/Flask App) --> B(Kafka Producer)
    end
    subgraph "Docker Containers"
        K0[Kafka Master]
        C[Zookeeper] --> K1[Kafka Broker 1]
        C[Zookeeper] --> K2[Kafka Broker 2]
        C[Zookeeper] --> K3[Kafka Broker 3]
        B --> K1
        E(Django/Flask/FastAPI Monitor) <-.-> K1
        E <-.-> C
        E <-.-> K0
    end
    style A fill:#0099ff,stroke:#333,stroke-width:2px
    style B fill:#999944,stroke:#333,stroke-width:2px
    style C fill:#ff9900,stroke:#333,stroke-width:2px
    style E fill:#0099ff,stroke:#333,stroke-width:2px
```

```mermaid
graph LR
    subgraph "Kafka"
        Python(Python)
        subgraph "Librerias"
            kafka
            graphviz
            numpy
        end
    end
    Python-->Exe1
    subgraph "FrontEnd"
        Python2(Python2)
        subgraph "Librerias2"
            kafka
            graphviz
            numpy
            pandas
        end
    end
    Python2-->Exe2
```