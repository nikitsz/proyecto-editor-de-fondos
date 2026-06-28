#====== Librerías ======
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.widgets import Button
from matplotlib.widgets import Button, Slider

#====== Definición de funciones ======

# Función para cargar la carpeta y seleccionar las imágenes y fondos
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

def carpeta_fondos(ruta):
    if os.path.exists(ruta):
        archivos = os.listdir(ruta)
        rutas = []
        for archivo in archivos:
            direccion = os.path.join(ruta, archivo)
            rutas.append(direccion)    
        print(f"Cargando {len(rutas)} imágenes de fondo automáticamente")
        return rutas
    else:
        print("La ruta no existe") 
        return []

# Función para reemplzara el fondo de la imagen
def nueva_imagen(matriz_Obj, matriz_fondo, tolerancia):
    copia_matriz = np.copy(matriz_Obj)
    
    transparencia_esquina = matriz_Obj[0, 0, 3] 
    
    if transparencia_esquina == 0:
        mascara = matriz_Obj[:, :, 3] == 0
    else:
        color_referencia = matriz_Obj[0, 0]
        
        
        diferencia = np.abs(matriz_Obj.astype(int) - color_referencia.astype(int))
        
        mascara = np.all(diferencia < tolerancia, axis=-1)
    
    copia_matriz[mascara] = matriz_fondo[mascara]
    
    return copia_matriz

def preparar_imagen(ruta_Obj, ruta_Fon):
    fondo = Image.open(ruta_Fon).convert("RGBA")
    imagen = Image.open(ruta_Obj).convert("RGBA")#prepara la imagen para mostrarla o algo asi nose :b es necesario guardarlo en una variable
    #if matriz_Obj.endsWith(".PNG"):
    #else:    
    T_imagen = imagen.size
    print("el tamaño de la imagen es:", imagen.size, "por lo que el tamaño del fondo se a modificado a:", imagen.size)#vemos el tamaño de la imagen (lo dice en la rubrica )
    fondo_ajustado = fondo.resize(T_imagen)
    matriz_Obj = np.array(imagen)
    matriz_fon = np.array(fondo_ajustado)
    return matriz_Obj, matriz_fon

#=====| Llamar funciones |=====#
 
"""print(matriz_Obj.shape)
print(matriz_fon.shape)"""

carpeta = carpeta_imagenes("Objetos/")
print(carpeta)
carp_fondos = carpeta_fondos("Fondos/")
print(carp_fondos)

if len(carp_fondos) < 2:
    print("\n[ERROR CRÍTICO] Se necesitan al menos 2 imágenes en la carpeta 'Fondos/'.")
    exit() 

try:
    matriz_Obj, matriz_fon1 = preparar_imagen(carpeta, carp_fondos[0])
    imagen_nuevo_fondo1 = nueva_imagen(matriz_Obj, matriz_fon1, 15)

    matriz_Obj, matriz_fon2 = preparar_imagen(carpeta, carp_fondos[1])
    imagen_nuevo_fondo2 = nueva_imagen(matriz_Obj, matriz_fon2, 15)


except Exception as e:
    print(f"\n[ERROR] Hubo un problema al procesar las imágenes: {e}")
    exit()

"""imagen_terminada = Image.fromarray(imagen_nuevo_fondo) # Convertimos la matriz matemática de vuelta a una imagen normal
imagen_terminada.show()"""

#=====| INTERFAZ GRÁFICA |======#
fig, ax = plt.subplots(figsize=(10, 6), facecolor="black")
imagen_interfaz = ax.imshow(matriz_Obj)
ax.set_title("Editor de Imágenes")
ax.axis('off')

estado = {"fondo_actual": 0}

esp_slider = plt.axes([0.25, 0.15, 0.5, 0.03], facecolor="lightgray")

slider_tol = Slider(esp_slider, "tolerancia", valmin=0, valmax=100, valinit=15, valstep=1)
slider_tol.label.set_color("white")
slider_tol.valtext.set_color("white")
# Creación de botones
esp_btn_original = plt.axes([0.02, 0.05, 0.17, 0.075])
esp_btn_fondo_1 = plt.axes([0.21, 0.05, 0.17, 0.075])
esp_btn_fondo_2 = plt.axes([0.40, 0.05, 0.17, 0.075])
esp_btn_guardar = plt.axes([0.59, 0.05, 0.17, 0.075])
esp_btn_reporte = plt.axes([0.78, 0.05, 0.17, 0.075])

btn_original = Button(esp_btn_original, "Imagen original")
btn_fondo_1 = Button(esp_btn_fondo_1, "Aplicar primer fondo")
btn_fondo_2 = Button(esp_btn_fondo_2, "Aplicar segundo fondo")
btn_guardar = Button(esp_btn_guardar, "Guardar Imagen")
btn_reporte = Button(esp_btn_reporte, "Reporte de Imagen")

# Función para botones
def actualizar_imagen(val=None):
    tol = slider_tol.val

    if estado["fondo_actual"] == 0:
        imagen_interfaz.set_data(matriz_Obj)
    elif estado["fondo_actual"] == 1:
        img_nueva = nueva_imagen(matriz_Obj, matriz_fon1, tol)
        imagen_interfaz.set_data(img_nueva)
    elif estado["fondo_actual"] == 2:
        img_nueva = nueva_imagen(matriz_Obj, matriz_fon2, tol)
        imagen_interfaz.set_data(img_nueva)
    plt.draw()            

slider_tol.on_changed(actualizar_imagen)

def accion_original(event):
    estado["fondo_actual"] = 0
    actualizar_imagen()

def accion_fondo_1(event):
    estado["fondo_actual"] = 1
    actualizar_imagen()

def accion_fondo_2(event):
    estado["fondo_actual"] = 2
    actualizar_imagen()

def accion_guardar(event):
    try:
        matriz_actual = imagen_interfaz.get_array()
        ahora = datetime.now()
        fecha_hora = ahora.strftime("%Y-%m-%d_%H-hrs_%M-min_%S-seg")
        nombre_archivo = f"resultado_{fecha_hora}.png"

        ruta_guardar = os.path.join("Objetos", nombre_archivo)
        img_final = Image.fromarray(matriz_actual)
        img_final.save(ruta_guardar)
        print(f"La imagen ha sido guardada como: {ruta_guardar}")
    except Exception as e:
        print(f"error al guardar: {e}")

def accion_reporte(event):
    try:
        ahora = datetime.now()
        fecha_hora = ahora.strftime("%d%m%Y_%H%M%S")
        nombre_archivo = f"reporte_{fecha_hora}.txt"
        
        tol = slider_tol.val
        
        transparencia_esquina = matriz_Obj[0, 0, 3]
        if transparencia_esquina == 0:
            mascara_fondo = matriz_Obj[:, :, 3] == 0
        else:
            color_referencia = matriz_Obj[0, 0]
            tolerancia = 15
            diferencia = np.abs(matriz_Obj.astype(int) - color_referencia.astype(int))
            mascara_fondo = np.all(diferencia < tolerancia, axis=-1)
        mascara_objeto = ~mascara_fondo
        cantidad_pixeles = np.sum(mascara_objeto)
        coordenadas_y, coordenadas_x = np.where(mascara_objeto)
        with open(nombre_archivo, "w") as archivo:
            archivo.write(f"Cantidad de píxeles del objeto: {cantidad_pixeles}\n\n")
            archivo.write("Coordenadas:\n\n")
            for x, y in zip(coordenadas_x, coordenadas_y):
                archivo.write(f"({x},{y})\n")
        print(f"\nel nombre del archivo es: {nombre_archivo}")        
    except Exception as e:
        print(f"error al hacer el reporte: {e}")

btn_original.on_clicked(accion_original)
btn_fondo_1.on_clicked(accion_fondo_1) 
btn_fondo_2.on_clicked(accion_fondo_2)
btn_guardar.on_clicked(accion_guardar)
btn_reporte.on_clicked(accion_reporte)
"""
btn_guardar.on_clicked()
"""

plt.show() 