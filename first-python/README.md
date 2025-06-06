# First Python Docker Project

Este proyecto tiene como propósito demostrar cómo crear y ejecutar un contenedor Docker para una aplicación Python sencilla.

## Prerequisitos

- Docker instalado en tu sistema.

## Construcción del contenedor

Para construir la imagen Docker, ejecuta el siguiente comando en el directorio del proyecto:

```bash
docker build -t first-python-app .
```

## Ejecución del contenedor

Para ejecutar el contenedor, utiliza el siguiente comando:

```bash
docker run --rm -p 5500:5000 --name first-pyex1 first-python-app:v1.0
```

El flag `--rm` asegura que el contenedor se elimine automáticamente después de su ejecución, y `-it` permite la interacción con el contenedor.

## Estructura del proyecto

Asegúrate que existen los archivos necesarios, como el `Dockerfile` y el script Python principal.

- `Dockerfile`: Define cómo se construye la imagen Docker.
- `app.py`: Archivo principal con el código Python.

