# weather_service.py
import requests
from datetime import datetime
from config import OPENWEATHER_API_KEY

def obtener_clima(ciudad):
    if not ciudad:
        raise ValueError("No se proporcionó ciudad.")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={OPENWEATHER_API_KEY}&units=metric&lang=es"
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()

        if datos.get("cod") != 200:
            raise Exception(datos.get("message", "Error desconocido."))

        zona_horaria = datos["timezone"]
        tiempo_local = datetime.utcfromtimestamp(datos["dt"] + zona_horaria)
        hora_local = tiempo_local.strftime("%H:%M:%S")

        clima = {
            "descripcion": datos["weather"][0]["description"].capitalize(),
            "temperatura": datos["main"]["temp"],
            "sensacion": datos["main"]["feels_like"],
            "humedad": datos["main"]["humidity"],
            "viento": datos["wind"]["speed"],
            "hora_local": hora_local,
            "icono": datos["weather"][0]["icon"]
        }
        return clima

    except requests.exceptions.RequestException as req_err:
        raise Exception("Error de red: " + str(req_err))
    except Exception as e:
        raise Exception("Error al obtener clima: " + str(e))
