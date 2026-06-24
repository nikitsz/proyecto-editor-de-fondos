#====== Librerías ======
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#Para verificar si un archivo/carpeta existe
#os.path.exists()

#Para unir dos direcciones en una
#os.path.join()

#Para identificar si un archivo es jpg o png
#os.path.splitext()


#====== Definición de funciones ======
def carpeta_imagenes(ruta):
    if os.path.exists(ruta):
        archivos = os.listdir(ruta)
        lis = " "
        for i in range(len(archivos)):
            img = f"\n{i+1}. {archivos[i]}"
            lis += img    
        print("Lista de imágenes: \n", lis)
        
        while True:
            num = input("Ingrese número de imagen: ") 
            try: 
                num_entero = int(num)
            except ValueError:
                print("Error: ingrese un número.")
                continue
            if num_entero < 1 or num_entero > len(archivos):
                print("Error, vuelva a ingresar número")
                continue
            imagen = archivos[int(num)-1]
            Image.open(imagen)
            break
    else:
        print("La ruta no existe")
        return None
    return imagen


#===== Llamar funciones =====#
carpeta = carpeta_imagenes("Objetos/")
print(carpeta)


"""""
#def cargar_imagen():
    objetos = "Objetos/"
    fondos = "Fondos/"
    lista_archivos = os.listdir(fondos)
    
    return lista_archivos
#print(cargar_imagen())"""