import tkinter as tk
from langdetect import detect
from iso639 import languages

# Función para obtener el nombre del idioma a partir del código ISO 639-1
def obtener_nombre_idioma(codigo_idioma):
    try:
        nombre_idioma = languages.get(part1=codigo_idioma).name
        return nombre_idioma
    except:
        return "Desconocido"

# Función para analizar el texto
def analizar_texto():
    texto = texto_entrada.get("1.0", "end-1c")
    palabras = texto.split()  # Dividir el texto en palabras utilizando espacios en blanco como separadores
    num_palabras = len(palabras)  # Contar el número de palabras en el texto
    # Ayuda a que se muestre el número de palabras
    resultado_texto.config(text=f"Número de palabras: {num_palabras}")
    caracteres = len(texto)
    # Ayuda a que se muestre el número de caracteres
    resultado_caracteres.config(text=f"Número de caracteres:{caracteres}")
    
    # Conteo de párrafos
    parrafos = texto.split("\n\n")  # Suponemos que los párrafos están separados por líneas en blanco
    num_parrafos = len(parrafos)
    # Mostrar el número de párrafos
    resultado_parrafos.config(text=f"Número de párrafos: {num_parrafos}")
    
    # Conteo de oraciones
    oraciones = texto.split(".")  # Suponemos que una oración termina con un punto "."
    num_oraciones = len(oraciones)
    # Mostrar el número de oraciones
    resultado_oraciones.config(text=f"Número de oraciones: {num_oraciones}")
    
    # Detección de idioma
    try:
        codigo_idioma = detect(texto)
        nombre_idioma = obtener_nombre_idioma(codigo_idioma)
        resultado_idioma.config(text=f"Idioma detectado: {nombre_idioma}")
    except:
        resultado_idioma.config(text="No se pudo detectar el idioma.")

# Crear la ventana de la aplicación
ventana = tk.Tk()
ventana.title("Herramienta de Análisis de Texto")
ventana.geometry("800x600")

# Etiqueta
etiqueta = tk.Label(ventana, text="Pega tu texto aquí:")
etiqueta.pack()

# Área de entrada de texto
texto_entrada = tk.Text(ventana, height=30, width=60)
texto_entrada.pack()

# Botón de análisis
boton_analizar = tk.Button(ventana, text="Analizar Texto", command=analizar_texto)
boton_analizar.pack()

# Crear etiquetas para mostrar los resultados
resultado_texto = tk.Label(ventana, text="")
resultado_texto.pack()
resultado_caracteres = tk.Label(ventana, text="")
resultado_caracteres.pack()
resultado_parrafos = tk.Label(ventana, text="")
resultado_parrafos.pack()
resultado_oraciones = tk.Label(ventana, text="")
resultado_oraciones.pack()
resultado_idioma = tk.Label(ventana, text="")
resultado_idioma.pack()

# Ejecutar la aplicación
ventana.mainloop()
