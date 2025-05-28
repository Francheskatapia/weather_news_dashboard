# dashboard.py
from weather_news_dashboard.weather_service import obtener_clima
from weather_news_dashboard.news_service import obtener_noticias_pais
from weather_news_dashboard.country_service import obtener_info_pais
import json
from datetime import date

def generar_dashboard(ciudad="La Serena", pais="Chile"):
    clima = obtener_clima(ciudad)
    noticias = obtener_noticias_pais(pais)
    info_pais = obtener_info_pais(pais)

    reporte = {
        "ciudad": ciudad,
        "pais": pais,
        "fecha": str(date.today()),
        "clima": clima,
        "noticias": noticias,
        "informacion_pais": info_pais
    }

    archivo_json = f"reporte_{date.today()}.json"
    with open(archivo_json, "w", encoding="utf-8") as f:
        json.dump(reporte, f, ensure_ascii=False, indent=2)

    print(f"Reporte guardado en {archivo_json}")
    return reporte
