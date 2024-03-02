# Reto Deimos Javier Romero

Reto de 8 casos de uso con Python y MongoDB

## Versiones de software utilizado:

- Python 3.10
- Docker 25.0.3

## Generación del entorno virtual e instalación de dependencias
```bash
python3 -m venv venv

. venv/bin/activate

pip install -r requirements
```

## Despliegue de la imagen de MongoDB en Docker
```bash
sudo docker build -t my-mongodb-image .

sudo docker run -d -p 27017:27017 --name my-mongodb-container my-mongodb-image
```

## Desplegar la API para los casos 6 y 8:
```bash
uvicorn fastapi_main:app
```


## Casos:

Los casos del 1 al 5 se incluyen en sus respectivos ficheros. Aquellos que generan información usable por otros casos incluyen una función para poder ser reutilizados, a parte de su propio main para su ejecución.

Los casos 6 y 8 se pueden encontrar en el fichero fastapi_main.py con sus respectivos endpoints cada uno. En el caso 8 se utilizó el script populate_mongodb_image.py para introducir los datos en el contenedor de MongoDB.

Para el caso 7, se utilizó el Dockerfile con una imagen simple de MongoDB sin ningún tipo de requisito de seguridad de usuarios. 
