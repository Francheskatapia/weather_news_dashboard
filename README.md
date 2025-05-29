# Weather News Dashboard 🌦️📰  

## Descripción 📝  
**Weather News Dashboard** es una aplicación Python que integra datos meteorológicos en tiempo real con noticias relevantes de cualquier región. Combina información de múltiples APIs públicas para ofrecer un reporte diario personalizable, con opción de exportación y envío automático por correo.  

---

## Características principales ✨  
✅ **Clima actual**: Temperatura, humedad, condiciones climáticas y pronóstico.  
✅ **Noticias por país**: Principales titulares o búsqueda por palabras clave.  
✅ **Datos de países**: Capital, población, moneda y más.  
✅ **Reportes combinados**: Correlación entre clima y noticias relevantes.  
✅ **Exportación**: Guarda reportes en JSON o texto plano.  
✅ **Automatización**: Envío programado de reportes diarios por Gmail.  

---

## APIs utilizadas 🔗  
- **OpenWeatherMap**: Datos meteorológicos.  
- **NewsAPI**: Noticias actualizadas.  
- **REST Countries**: Información geográfica.  
- **Gmail API**: Automatización de correos.  

---

## Estructura del proyecto 📂  
weather_news_dashboard/
├── main.py # Punto de entrada
├── config.py # Configuración (API keys directamente aquí)
├── weather_service.py # Lógica de clima (OpenWeatherMap)
├── news_service.py # Lógica de noticias (NewsAPI)
├── country_service.py # Lógica de países (REST Countries)
├── dashboard.py # Generación de reportes
├── gmail_service.py # Envío automático (Gmail API)
└── requirements.txt # Dependencias

---

## Configuración ⚙️  
1. **Clonar repositorio**:  
   ```bash  
   git clone https://github.com/tu-usuario/weather-news-dashboard.git  

2. **Instalar Dependencias**:
    ```bash
    pip install -r requirements.txt 

3. **Configurar APIs**:
    Revisar config_example.py y agregar tus API keys:
    ```bash
    OPENWEATHER_API_KEY = "tu_api_key"  
    NEWSAPI_API_KEY = "tu_api_key"  
    GMAIL_CREDENTIALS = "credenciales_gmail.json"  # Opcional para automatización  

---

## Uso 🚀
Ejecutar desde la terminal:
    ```bash
    python main.py --ciudad "La Serena" --pais "Chile"  

Opciones disponibles:
--ciudad: Nombre de la ciudad (requerido).

--pais: País para noticias/datos (opcional, default: Chile).

--exportar_json: Guarda el reporte en reporte.json.

--enviar_correo: Programa envío diario (requiere Gmail API).

---

## Documentación técnica 📚
--Manejo de errores: Captura excepciones de APIs (HTTP 404, 500, etc.).

--Logging: Registra solicitudes en consola.

--Validaciones: Parámetros obligatorios y formatos de ciudad/pais.

---

## Licencia 📜
