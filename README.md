# 🌧️ Sensor de Lluvia IoT – AWS IoT Core + Lambda + CloudWatch

**Proyecto creado por Anthony Guzmán**

Este proyecto es una simulación de un **Sensor de Lluvia IoT**, desarrollado con **Python** y conectado a los servicios de **AWS IoT Core**, **AWS Lambda** y **AWS CloudWatch Logs**. El objetivo principal es enviar datos desde un dispositivo simulado en Visual Studio Code (o cualquier entorno Python) hacia la nube de AWS, procesarlos automáticamente y visualizar su comportamiento en tiempo real.

---

## 🚀 Descripción del Proyecto

El sistema envía datos JSON que representan:

* 💧 **Presencia de lluvia** (`true` / `false`)
* 🌡️ **Intensidad de la lluvia** (`0.00 – 1.00`)

Estos datos se publican en el tópico MQTT:

`sensor/lluvia`

**AWS IoT Core** recibe esta información y, mediante una **IoT Rule**, activa una función **AWS Lambda** que interpreta la intensidad y determina el estado del clima en tiempo real:

* 🌦️ Lluvia moderada
* 🌧️ Lluvia fuerte
* ☀️ No está lloviendo

Los resultados procesados se almacenan automáticamente en **CloudWatch Logs**, lo que permite verificar la comunicación y la lógica entre el sensor, IoT Core y Lambda.

---

## 🧩 Arquitectura del Proyecto

**Python (VSCode)** → **AWS IoT Core** → **IoT Rule** → **AWS Lambda** → **CloudWatch Logs**



---

## 🛠️ Tecnologías Utilizadas

* **Python** + Paho MQTT
* **AWS IoT Core**
* **AWS Lambda**
* **AWS CloudWatch Logs**
* **Certificados SSL/TLS** (para conexión segura con IoT Core)

---

## ▶️ Cómo ejecutar el proyecto 💻

Para poner en marcha el simulador del sensor, sigue estos pasos en tu terminal (BASH, PowerShell, CMD, etc.):

### 1. Instalar dependencias

Asegúrate de tener Python instalado. El proyecto requiere la librería `paho-mqtt` para la comunicación MQTT.

```bash
pip install paho-mqtt

```
2. Ejecutar el script
Ejecuta el script principal de Python para iniciar la simulación del envío de datos a AWS IoT Core.
```
python sensor_lluvia.py

```
## 👨‍💻 Autor

**Anthony Guzmán**  
Estudiante de Desarrollo de Software – ITLA  
LinkedIn: https://www.linkedin.com/in/anthonyguzm/


