import ssl
import paho.mqtt.client as mqtt
import time
import json
import random

# Parámetros de conexión
endpoint = ""
port = 8883
topic = "sensor/lluvia"

client = mqtt.Client()

client.tls_set(
    ca_certs="",
    certfile="",
    keyfile="",
    tls_version=ssl.PROTOCOL_TLSv1_2
)

client.connect(endpoint, port)

for _ in range(5):
    intensidad = round(random.uniform(0.0, 1.0), 2)
    lluvia = True

    payload = json.dumps({
        "lluvia": lluvia,
        "intensidad": intensidad
    })

    client.publish(topic, payload)
    print("Enviando:", payload)
    time.sleep(2)

client.disconnect()
