import tkinter as tk
from tkinter import messagebox, scrolledtext
from weather_news_dashboard.weather_service import obtener_clima
from weather_news_dashboard.news_service import obtener_noticias_pais
from weather_news_dashboard.country_service import obtener_info_pais
from weather_news_dashboard.dashboard import generar_dashboard

# 🧠 Funciones de lógica
def mostrar_clima():
    ciudad = entry_ciudad.get().strip()
    try:
        clima = obtener_clima(ciudad)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"🌤️ Clima en {ciudad}:\n")
        resultado_text.insert(tk.END, f"{clima['descripcion']}\n")
        resultado_text.insert(tk.END, f"Temperatura: {clima['temperatura']}°C\n")
        resultado_text.insert(tk.END, f"Sensación térmica: {clima['sensacion']}°C\n")
        resultado_text.insert(tk.END, f"Humedad: {clima['humedad']}%\n")
        resultado_text.insert(tk.END, f"Viento: {clima['viento']} m/s\n")
        resultado_text.insert(tk.END, f"Hora local: {clima['hora_local']}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_noticias():
    pais = entry_pais.get().lower().strip()
    if pais == "chile":
        pais = "cl"
    categoria = categoria_var.get()
    try:
        noticias = obtener_noticias_pais(pais, categoria)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"📰 Noticias de {pais.upper()} - Categoría: {categoria}\n\n")
        for n in noticias[:5]:
            resultado_text.insert(tk.END, f"- {n['titulo']} ({n['fuente']})\n")
            resultado_text.insert(tk.END, f"  {n['url']}\n\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_info_pais():
    pais = entry_pais.get().strip()
    try:
        info = obtener_info_pais(pais)
        resultado_text.delete(1.0, tk.END)
        resultado_text.insert(tk.END, f"🌎 Información de {info['pais']}:\n")
        resultado_text.insert(tk.END, f"Capital: {info['capital']}\n")
        resultado_text.insert(tk.END, f"Población: {info['poblacion']}\n")
        resultado_text.insert(tk.END, f"Moneda: {info['moneda']}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def guardar_reporte():
    ciudad = entry_ciudad.get().strip()
    pais = entry_pais.get().strip()
    try:
        generar_dashboard(ciudad, pais)
        messagebox.showinfo("Éxito", f"Reporte guardado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# 🖼️ Interfaz Gráfica
ventana = tk.Tk()
ventana.title("Dashboard de Clima, Noticias y Países")
ventana.geometry("700x600")
ventana.configure(bg="#F5F5F5")

# ------- Sección de Entradas --------
frame_entradas = tk.Frame(ventana, bg="#F5F5F5")
frame_entradas.pack(pady=10)

tk.Label(frame_entradas, text="Ciudad:", bg="#F5F5F5", font=("Helvetica", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_ciudad = tk.Entry(frame_entradas, font=("Helvetica", 12), width=20)
entry_ciudad.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text="País:", bg="#F5F5F5", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_pais = tk.Entry(frame_entradas, font=("Helvetica", 12), width=20)
entry_pais.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text="Categoría de noticias:", bg="#F5F5F5", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
categorias = ["general", "business", "entertainment", "health", "science", "sports", "technology"]
categoria_var = tk.StringVar(value="general")
dropdown_categoria = tk.OptionMenu(frame_entradas, categoria_var, *categorias)
dropdown_categoria.config(font=("Helvetica", 11), bg="#E0E0E0")
dropdown_categoria.grid(row=2, column=1, padx=5, pady=5, sticky="we")

# ------- Botones --------
frame_botones = tk.Frame(ventana, bg="#F5F5F5")
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="🌤️ Ver Clima", command=mostrar_clima, bg="#BBDEFB", font=("Helvetica", 11), width=15).grid(row=0, column=0, padx=10, pady=5)
tk.Button(frame_botones, text="📰 Ver Noticias", command=mostrar_noticias, bg="#C8E6C9", font=("Helvetica", 11), width=15).grid(row=0, column=1, padx=10, pady=5)
tk.Button(frame_botones, text="🌎 Ver Info País", command=mostrar_info_pais, bg="#FFE082", font=("Helvetica", 11), width=15).grid(row=0, column=2, padx=10, pady=5)
tk.Button(frame_botones, text="💾 Guardar Reporte", command=guardar_reporte, bg="#FFAB91", font=("Helvetica", 11), width=20).grid(row=1, column=0, columnspan=3, pady=10)

# ------- Área de resultados --------
resultado_text = scrolledtext.ScrolledText(ventana, width=80, height=25, font=("Helvetica", 10), wrap="word")
resultado_text.pack(padx=10, pady=10)

ventana.mainloop()
