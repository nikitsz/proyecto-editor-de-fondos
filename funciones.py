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



#===== Llamar funciones =====#
carpeta = carpeta_imagenes("Objetos/")
print(carpeta)

carp_fondos = carpeta_imagenes("Fondos/")
print(carp_fondos)

fondo = Image.open(carp_fondos)
imagen = Image.open(carpeta)#prepara la imagen para mostrarla o algo asi nose :b es necesario guardarlo en una variable
T_imagen = imagen.size
print("el tamaño de la imagen es:", imagen.size, "por lo que el tamaño del fondo es:", imagen.size)#vemos el tamaño de la imagen (lo dice en la rubrica )
fondo_ajustado = fondo.resize(T_imagen)

#fondo_ajustado.show()#muestra la imagen en la pantalla
#imagen.show() #estos 2 nos servirian para mostrar la imagen pero primero tenemos que convertir las imagenes a matrices
matriz_Obj = np.array(imagen)
matriz_fon = np.array(fondo_ajustado)
print(matriz_Obj.shape)
print(matriz_fon.shape)

#Para conocer los colore de un punto específico de la matriz
#color_pixel = matriz_Obj[0, 0]
#print("color del pixel: ", color_pixel)

#0 = Rojo
#1 = Verde
#2 = Azul

#canal_rojo = matriz_Obj[:, :, 0] #Los ":" se ocupan para seleccionar todas las filas y columnas de la matriz

#Necesitaremos el np.copy para guardar la imagen original en una copia
#matriz_mod = np.copy(matriz_Obj)

#===== Acceder a colores de referencia ======#
#Para las imagenes, generalmente el color del fondo liso es el mismo del primer pixel ([0, 0])
#color_referencia = matriz_Obj[0, 0]
#print("El color de referencia es: ", color_referencia)

#===== Creación de la función de la nueva imagen =====#
def nueva_imagen(matriz_Obj, matriz_fondo):
    copia_matriz = np.copy(matriz_Obj)
    color_referencia = matriz_Obj[0, 0]
    mascara = matriz_Obj == color_referencia