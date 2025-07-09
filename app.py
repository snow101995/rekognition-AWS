import boto3
import json
import uuid
import logging
from datetime import datetime
from botocore.exceptions import BotoCoreError, ClientError

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración
bucket = 'analisis-imagenes'
imagen = 'personas.jpeg'
tabla_dynamodb = 'ResultadosRekognition'

# Clientes
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
tabla = dynamodb.Table(tabla_dynamodb)

def detectar_rostros(bucket, key):
    try:
        logger.info(f"Analizando imagen: {key}")
        response = rekognition.detect_faces(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            Attributes=['ALL']
        )
        return response.get('FaceDetails', [])
    except ClientError as e:
        logger.error(f"Error de cliente AWS: {e.response['Error']['Message']}")
    except BotoCoreError as e:
        logger.error(f"Error general de boto3: {str(e)}")
    return []

def guardar_resultado(face, imagen):
    try:
        emocion = max(face['Emotions'], key=lambda x: x['Confidence'])

        item = {
            'id': str(uuid.uuid4()),
            'timestamp': datetime.utcnow().isoformat(),
            'imagen': imagen,
            'emocion': emocion['Type'],
            'confianza_emocion': str(round(emocion['Confidence'], 2)),
            'confianza_rostro': str(round(face['Confidence'], 2)),
        }

        tabla.put_item(Item=item)
        return item
    except Exception as e:
        logger.error(f"Error al guardar en DynamoDB: {str(e)}")
        return None

def analizar_imagen():
    rostros = detectar_rostros(bucket, imagen)
    if not rostros:
        logger.warning("No se detectaron rostros en la imagen.")
        return

    resultados = []
    for rostro in rostros:
        resultado = guardar_resultado(rostro, imagen)
        if resultado:
            resultados.append(resultado)

    logger.info("Análisis completado. Resultados:")
    logger.info(json.dumps(resultados, indent=2))

if __name__ == '__main__':
    analizar_imagen()

