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
            break
    else:
        print("La ruta no existe")
        return None
    return os.path.join(ruta, imagen)
"""
def fondos(ruta):
    if os.path.exists(ruta):
        archivos = os.listdir(ruta)
        lis = " "
        for i in range(len(archivos)):
            img = f"\n{i+1}. {archivos[i]}"
            lis += img    
        fon = f"Lista de fondos: \n {lis}"
    return fon
"""


#===== Llamar funciones =====#
carpeta = carpeta_imagenes("Objetos/")
print(carpeta)

carp_fondos = ("Fondos/")
print(carp_fondos)

fondos = carpeta_imagenes(carp_fondos)
print(fondos)


imagen = Image.open(carpeta)#prepara la imagen para mostrarla o algo asi nose :b es necesario guardarlo en una variable
print("el tamaño de la imagen es:", imagen.size)#vemos el tamaño de la imagen (lo dice en la rubrica )
imagen.show()#muestra la imagen en la pántalla

#########################################################
#¡¡¡¡¡¡¡¡¡¡¡¡¡IMPORTANTE¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡
#ningun cambio realizado aqui es definitivo solamente estaba probando codigos que nos podrian servir
#y gemini me dijo que no era importante la interfaz pero yo lo quiero hacer con interfaz
#elpepe67
#########################################################
"""""
#def cargar_imagen():
    objetos = "Objetos/"
    fondos = "Fondos/"
    lista_archivos = os.listdir(fondos)
    
    return lista_archivos
#print(cargar_imagen())"""