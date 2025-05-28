# country_service.py
import requests

def obtener_info_pais(nombre_pais):
    url = f"https://restcountries.com/v3.1/name/{nombre_pais}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()

        if not datos:
            raise Exception("No se encontró información del país.")

        pais = datos[0]

        capital = pais.get("capital", ["No disponible"])[0]
        poblacion = pais.get("population", "No disponible")

        monedas = pais.get("currencies", {})
        moneda_nombre = "No disponible"
        moneda_codigo = "No disponible"
        for codigo, info in monedas.items():
            moneda_nombre = info.get("name", "Desconocida")
            moneda_codigo = codigo
            break

        return {
            "pais": pais.get("name", {}).get("common", "Desconocido"),
            "capital": capital,
            "poblacion": poblacion,
            "moneda": f"{moneda_nombre} ({moneda_codigo})"
        }

    except requests.exceptions.RequestException as e:
        raise Exception("Error de red al obtener país: " + str(e))
    except Exception as e:
        raise Exception("Error general: " + str(e))
