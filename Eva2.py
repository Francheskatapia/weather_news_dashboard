import requests
from gmail import get_gmail_service, send_email
import datetime

# Cambia esto por tu email
TO_EMAIL = "redes.avanzadas29@gmail.com"

def get_weather():
    API_KEY = "8f9539d0670489d1bf848349ded9438a"
    CITY = "La Serena,CL"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric&lang=es"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_desc = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        return (f"Clima en La Serena:\n"
                f"- Estado: {weather_desc}\n"
                f"- Temperatura: {temp}°C\n"
                f"- Sensación térmica: {feels_like}°C\n"
                f"- Humedad: {humidity}%\n"
                f"- Viento: {wind_speed} m/s")
    else:
        return "No se pudo obtener el clima."

def get_news():
    API_KEY = "5e16c55de71140f6abb016361e1d8d4c"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}&pageSize=3"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data.get('articles'):
        articles = data['articles']
        news_list = []
        for article in articles:
            title = article['title']
            source = article['source']['name']
            url = article['url']
            news_list.append(f"- {title} ({source})\n  {url}")
        return "Noticias destacadas:\n" + "\n".join(news_list)
    else:
        return "No se encontraron noticias destacadas."

def main():
    clima = get_weather()
    noticias = get_news()
    fecha = datetime.datetime.now().strftime("%d/%m/%Y")
    contenido = f"Reporte diario ({fecha}):\n\n{clima}\n\n{noticias}"
    
    service = get_gmail_service()
    send_email(service, TO_EMAIL, f"Reporte Diario - {fecha}", contenido)

if __name__ == "__main__":
    main()



