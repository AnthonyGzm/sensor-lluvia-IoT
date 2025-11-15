import json

def lambda_handler(event, context):
    print("Datos recibidos del sensor:", event)

    lluvia = event.get("lluvia")
    intensidad = event.get("intensidad")

    if lluvia:
        if intensidad < 0.3:
            estado = "Lluvia ligera"
        elif intensidad < 0.7:
            estado = "Lluvia moderada"
        else:
            estado = "Lluvia fuerte"
    else:
        estado = "No está lloviendo"

    print("Estado procesado:", estado)

    return {
        "statusCode": 200,
        "body": json.dumps({"estado": estado})
    }
