#importar librerías 

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#creación de la clase pokémon 

class Pokemon:
    
    def __init__(self, Nombre, Tipo1, Tipo2, ATK, SPA, DEF, SPDEF, speed):
        self.Nombre = Nombre
        self.Tipo1 = Tipo1
        self.Tipo2 = Tipo2
        self.ATK = ATK
        self.SPA = SPA
        self.DEF = DEF
        self.SPDEF = SPDEF
        self.speed = speed 

# Crear instancias de la clase Pokemon y almacenarlas en un diccionario

pokemons = {
    
    #tipo fuego 
    "charizard": Pokemon("Charizard", "Fuego", "Volador", 78, 159, 78, 115, 100),
    "arcanine": Pokemon("Arcanine", "Fuego", None, 90, 100, 80, 80, 95),
    "blaziken": Pokemon("Blaziken", "Fuego", "Lucha", 80, 110, 70, 70, 80),
    "infernape": Pokemon("Infernape", "Fuego", "Lucha", 76, 104, 71, 71, 108),
    "chandelure": Pokemon("Chandelure", "Fuego", "Fantasma", 60, 145, 90, 90, 80),
    "volcanion": Pokemon("Volcanion", "Fuego", "Agua", 110, 130, 120, 90, 70),
    "incineroar": Pokemon("Incineroar", "Fuego", "Siniestro", 115, 80, 90, 90, 60),
    "volcarona": Pokemon("Volcarona", "Bicho", "Fuego", 60, 135, 60, 105, 100),
    "talonflame": Pokemon("Talonflame", "Fuego", "Volador", 81, 74, 71, 69, 126),
    "salazzle": Pokemon("Salazzle", "Veneno", "Fuego", 64, 111, 60, 60, 117),
    "turtonator": Pokemon("Turtonator", "Fuego", "Dragón", 78, 91, 85, 85, 36),
    "blacephalon": Pokemon("Blacephalon", "Fuego", "Fantasma", 107, 151, 53, 79, 107),
    #tipo agua
    "blastoise": Pokemon("Blastoise", "Agua", None, 79, 85, 100, 105, 78),
    "gyarados": Pokemon("Gyarados", "Agua", "Volador", 95, 60, 79, 100, 81),
    "vaporeon": Pokemon("Vaporeon", "Agua", None, 110, 85, 95, 65, 65),
    "swampert": Pokemon("Swampert", "Agua", "Tierra", 100, 85, 90, 90, 60),
    "empoleon": Pokemon("Empoleon", "Agua", "Acero", 84, 111, 101, 101, 60),
    "greninja": Pokemon("Greninja", "Agua", "Siniestro", 72, 97, 67, 71, 122),
    "primarina": Pokemon("Primarina", "Agua", "Hada", 74, 126, 74, 116, 60),
    "inteleon": Pokemon("Inteleon", "Agua", None, 70, 125, 65, 80, 120),
    "toxapex": Pokemon("Toxapex", "Agua", "Veneno", 50, 60, 152, 142, 35),
    "milotic": Pokemon("Milotic", "Agua", None, 95, 100, 79, 125, 81),
    "kingler": Pokemon("Kingler", "Agua", None, 130, 75, 115, 50, 75),
    #tipo dragón 
    "dragonite": Pokemon("Dragonite", "Dragón", "Volador", 91, 134, 95, 100, 80),
    "salamence": Pokemon("Salamence", "Dragón", "Volador", 95, 110, 90, 90, 100),
    "garchomp": Pokemon("Garchomp", "Dragón", "Tierra", 108, 130, 95, 85, 102),
    "hydreigon": Pokemon("Hydreigon", "Dragón", "Siniestro", 92, 125, 90, 90, 98),
    "goodra": Pokemon("Goodra", "Dragón", None, 100, 110, 150, 150, 80),
    "noivern": Pokemon("Noivern", "Dragón", "Volador", 85, 97, 80, 80, 123),
    "haxorus": Pokemon("Haxorus", "Dragón", None, 147, 60, 90, 70, 97),
    "rayquaza": Pokemon("Rayquaza", "Dragón", "Volador", 105, 150, 90, 90, 95),
    "altaria": Pokemon("Altaria", "Dragón", "Volador", 70, 70, 90, 105, 80),
    "kingdra": Pokemon("Kingdra", "Agua", "Dragón", 75, 95, 95, 95, 85),
    #tipo hada
   "clefable": Pokemon("Clefable", "Hada", None, 70, 95, 73, 90, 60),
    "togekiss": Pokemon("Togekiss", "Hada", "Volador", 85, 80, 95, 115, 80),
    "gardevoir": Pokemon("Gardevoir", "Hada", "Psíquico", 68, 125, 65, 115, 80),
    "azumarill": Pokemon("Azumarill", "Hada", "Agua", 50, 50, 80, 80, 50),
    "florges": Pokemon("Florges", "Hada", None, 78, 65, 68, 112, 75),
    "sylveon": Pokemon("Sylveon", "Hada", None, 95, 65, 65, 130, 60),
    "mimikyu": Pokemon("Mimikyu", "Hada", "Fantasma", 90, 80, 80, 105, 96),
    "primarina": Pokemon("Primarina", "Agua", "Hada", 74, 126, 74, 116, 60),
    "tapu lele": Pokemon("Tapu Lele", "Psíquico", "Hada", 85, 75, 70, 115, 95)
    #tipo ácero
    
}

# deposita los datos en un archivo .csv  

def guardar_en_csv(pokemon):
    with open('pokemons.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([pokemon.Nombre, pokemon.ATK, pokemon.SPA, pokemon.DEF, pokemon.SPDEF, pokemon.speed])

#comprueba que el pokémon se encuentre registrado o se haya escrito correctamente 

def obtener_pokemon(nombre_pokemon):
    if nombre_pokemon in pokemons:
        return pokemons[nombre_pokemon]
    else:
        print("No se encontró el Pokémon especificado.")
        return None

a = input("Introduce el nombre del Pokémon que quieres ver sus estadisticas: ").lower()
b = input("Introduce el nombre del Pokémon para comparar con el anterior: ").lower()

primer_pokemon = obtener_pokemon(a)
segundo_pokemon = obtener_pokemon(b)

#definir que pokémon es mejor
def elección_mejor():
    pk = 0
    pk2 = 0 
    
    print("\n**************************************")
    if primer_pokemon.ATK >= segundo_pokemon.ATK:
        print(f"{a} es mejor en ataque")
        pk+=1
    else:
        print(f"{b} es mejor en ataque")
        pk2+=1
    
    if primer_pokemon.SPA >= segundo_pokemon.SPA:
        print(f"{a} es mejor en ataque especial")
        pk+=1
    else:
        print(f"{b} es mejor en ataque especial")
        pk2+=1   
    
    if primer_pokemon.DEF >= segundo_pokemon.DEF:
        print(f"{a} es mejor en defensa")
        pk+=1
    else:
        print(f"{b} es mejor en defensa")
        pk2+=1    
    
    if primer_pokemon.SPDEF >= segundo_pokemon.SPDEF:
        print(f"{a} es mejor en defensa especial")
        pk+=1
    else:
        print(f"{b} es mejor en defensa especial")
        pk2+=1  
        
    if primer_pokemon.speed >= segundo_pokemon.speed:
        print(f"{a} es mejor en velocidad")
        pk+=1
    else:
        print(f"{b} es mejor en  velocidad")
        pk2+=1    

    if pk >= pk2:
        print(f"deberías elegir a {a}")
        
    else:
        print(f"deberías elegir a {b}")
      
elección_mejor()

# condicional para el gráfico de araña

if primer_pokemon and segundo_pokemon:
    print("\n***********************************")
    print(f"\nEstadísticas del primer Pokémon {a}:")
    print(f"\nATK: {primer_pokemon.ATK}")
    print(f"SPA: {primer_pokemon.SPA}")
    print(f"DEF: {primer_pokemon.DEF}")
    print(f"SPDEF: {primer_pokemon.SPDEF}")
    print(f"Speed: {primer_pokemon.speed}")
    print("\n***********************************")
    print(f"\nEstadísticas del segundo Pokémon {b}:")
    print(f"\nATK: {segundo_pokemon.ATK}")
    print(f"SPA: {segundo_pokemon.SPA}")
    print(f"DEF: {segundo_pokemon.DEF}")
    print(f"SPDEF: {segundo_pokemon.SPDEF}")
    print(f"Speed: {segundo_pokemon.speed}")
    

#gráfico de araña

    stats1 = [primer_pokemon.ATK, primer_pokemon.SPA, primer_pokemon.DEF, primer_pokemon.SPDEF, primer_pokemon.speed]
    stats2 = [segundo_pokemon.ATK, segundo_pokemon.SPA, segundo_pokemon.DEF, segundo_pokemon.SPDEF, segundo_pokemon.speed]
    labels = ["ATK", "SPA", "DEF", "SPDEF", "Speed"]

    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    stats1 = np.concatenate((stats1, [stats1[0]]))  # Cerrar el ciclo
    stats2 = np.concatenate((stats2, [stats2[0]]))  # Cerrar el ciclo
    angles = np.concatenate((angles, [angles[0]]))  # Cerrar el ciclo

    plt.figure(figsize=(4, 4))
    plt.polar(angles, stats1, label=primer_pokemon.Nombre)
    plt.fill(angles, stats1, alpha=0.25)
    plt.polar(angles, stats2, label=segundo_pokemon.Nombre)
    plt.fill(angles, stats2, alpha=0.25)
    plt.xticks(angles[:-1], labels)
    plt.title('Comparación de Estadísticas')
    plt.legend()
    plt.show()