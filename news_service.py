# news_service.py
import requests
from weather_news_dashboard.config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2/top-headlines"

def obtener_noticias_pais(pais, categoria=None):
    if not pais:
        raise ValueError("Debes ingresar un código de país (por ejemplo, 'cl').")

    params = {
        "country": pais.lower(),  # siempre en minúscula
        "apiKey": NEWS_API_KEY
    }
    if categoria:
        params["category"] = categoria

    response = requests.get(BASE_URL, params=params)
    datos = response.json()

    if datos.get("status") != "ok":
        raise Exception(f"Error al obtener noticias: {datos.get('message', 'Error desconocido')}")

    noticias = []
    for articulo in datos.get("articles", []):
        noticias.append({
            "titulo": articulo.get("title"),
            "descripcion": articulo.get("description"),
            "url": articulo.get("url"),
            "fuente": articulo.get("source", {}).get("name")
        })

    return noticias

def buscar_noticias_por_termino(termino, pais):
    if not pais or not termino:
        raise ValueError("Debes ingresar un país y un término de búsqueda.")

    url = "https://newsapi.org/v2/everything"
    params = {
        "q": termino,
        "language": "es",
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }

    response = requests.get(url, params=params)
    datos = response.json()

    if datos.get("status") != "ok":
        raise Exception(f"Error al buscar noticias: {datos.get('message', 'Error desconocido')}")

    noticias = []
    for articulo in datos.get("articles", []):
        noticias.append({
            "titulo": articulo.get("title"),
            "descripcion": articulo.get("description"),
            "url": articulo.get("url"),
            "fuente": articulo.get("source", {}).get("name")
        })

    return noticias
