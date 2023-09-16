from PIL import Image
import os
import shutil

#carpeta de descargas
downloadsfolder = "put your folder name"
#carpeta de desetino 
folder = "put your destiny folder"

if __name__ == "__main__":
    for filename in os.listdir(downloadsfolder):
        # Obtener la ruta completa del archivo en la carpeta de descargas
        full_path = os.path.join(downloadsfolder, filename)
        
        # Separar el nombre y la extensión del archivo
        name, extension = os.path.splitext(filename)
        
        # elije la extensión de los archivos que deseas separar para moverlos
        if extension.lower() in ['.py']:
            # Construir la ruta de destino en la carpeta respectiva
            destination_path = os.path.join(folder, filename)
            
            # Mover el archivo de descargas a la carpeta respectiva
            shutil.move(full_path, destination_path)
            
            print(f"Archivo '{filename}' movido a la carpeta respectiva.")

print("Proceso completado.")

