#primer commit

"""""
#def cargar_imagen():
    objetos = "Objetos/"
    fondos = "Fondos/"
    lista_archivos = os.listdir(fondos)
    
    return lista_archivos
#print(cargar_imagen())"""

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
#fondo_ajustado.show()#muestra la imagen en la pantalla
#imagen.show() #estos 2 nos servirian para mostrar la imagen pero primero tenemos que convertir las imagenes a matrices


#Para conocer los colores de un punto específico de la matriz:
#color_pixel = matriz_Obj[0, 0]
#print("color del pixel: ", color_pixel)

#0 = Rojo
#1 = Verde
#2 = Azul

#==== Los ":" se ocupan para seleccionar todas las filas y columnas de la matriz ====
#canal_rojo = matriz_Obj[:, :, 0]

#Necesitaremos el np.copy para guardar la imagen original en una copia
#matriz_mod = np.copy(matriz_Obj)

#===== Acceder a colores de referencia ======#
#Para las imagenes, generalmente el color del fondo liso es el mismo del primer pixel ([0, 0])
#color_referencia = matriz_Obj[0, 0]
#print("El color de referencia es: ", color_referencia)

#Para verificar si un archivo/carpeta existe
#os.path.exists()

#Para unir dos direcciones en una
#os.path.join()

#Para identificar si un archivo es jpg o png
#os.path.splitext()


def nueva_imagen(matriz_Obj, matriz_fondo):
    copia_matriz = np.copy(matriz_Obj)
    color_referencia = matriz_Obj[0, 0]    
    mascara = np.all(matriz_Obj == color_referencia, axis=-1)
    copia_matriz[mascara] = matriz_fondo[mascara]
    return copia_matriz