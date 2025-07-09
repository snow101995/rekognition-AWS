# 🔍 AWS Rekognition con Lambda + DynamoDB

Este proyecto es una función AWS Lambda escrita en Python. Su propósito es analizar imágenes usando Amazon Rekognition para detectar rostros y emociones, y luego guardar los resultados en una tabla DynamoDB.

## 🚀 ¿Cómo funciona?

1. Un usuario sube una imagen a un bucket S3.
2. El evento activa la función Lambda automáticamente.
3. Lambda invoca Amazon Rekognition para analizar la imagen.
4. Se detectan rostros y emociones en la imagen.
5. Los resultados son almacenados en la tabla DynamoDB `ResultadosRekognition`.

## 🧱 Servicios utilizados

- **Amazon S3**: Almacenamiento de imágenes.
- **AWS Lambda**: Procesamiento serverless.
- **Amazon Rekognition**: Análisis de imágenes (detección de rostros, emociones).
- **Amazon DynamoDB**: Almacenamiento de resultados del análisis.

## 📁 Estructura del proyecto

- `app.py`: Código principal de la función Lambda.
- `requirements.txt`: Lista de dependencias Python.
- `.gitignore`: Ignora archivos innecesarios o sensibles.
- `README.md`: Este archivo con la documentación del proyecto.
- `template.yaml`: Plantilla opcional para despliegue con AWS SAM.

## ✅ Requisitos

- Un bucket S3 configurado para activar la función Lambda al subir imágenes.
- Una tabla DynamoDB llamada `ResultadosRekognition` con `id` como clave primaria.
- Permisos adecuados en el rol de ejecución de Lambda para acceder a S3, Rekognition y DynamoDB.

## 📌 Notas adicionales

Este proyecto está diseñado para ser simple, modular y fácil de integrar con otros servicios AWS. Puedes extenderlo para agregar notificaciones, validaciones, o interfaces web en el futuro si lo deseas.
