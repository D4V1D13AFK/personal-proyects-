import tkinter as tk

# Función para analizar el texto
def analizar_texto():
    palabras_excluidas = ["y", "o", "el", "la", "de", "en", "un", "una", "para","es"]
    palabras_clave = []
    texto = texto_entrada.get("1.0", "end-1c")
    palabras = texto.split()  # Dividir el texto en palabras utilizando espacios en blanco como separadores
    num_palabras = len(palabras)  # Contar el número de palabras en el texto
    # Ayuda a que se muestre el número de palabras
    resultado_texto.config(text=f"Número de palabras: {num_palabras}")
    caracteres = len(texto)
    # Ayuda a que se muestre el número de caracteres
    resultado_caracteres.config(text=f"Número de caracteres:{caracteres}")
    
    # Crear un diccionario para almacenar la frecuencia de palabras
    frecuencia_palabras = {}
    
    for palabra in palabras:
        # Convertir la palabra a minúsculas para hacer la búsqueda insensible a mayúsculas
        palabra = palabra.lower()
        if palabra in palabras_excluidas:
            continue
        
        # Si la palabra ya está en el diccionario, aumenta su frecuencia
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    # Buscar palabras clave (aquí se consideran aquellas que aparecen más de una vez)
    for palabra, frecuencia in frecuencia_palabras.items():
        if frecuencia > 1:
            palabras_clave.append(palabra)
    
    # Mostrar el resultado de palabras clave
    resultado_palabras_clave.config(text=f"Palabras clave: {', '.join(palabras_clave)}")
    
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
resultado_palabras_clave = tk.Label(ventana, text="")
resultado_palabras_clave.pack()

# Ejecutar la aplicación
ventana.mainloop()
