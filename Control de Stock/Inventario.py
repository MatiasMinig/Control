from Validador import *

"""Inventario de articulos en formato de diccionario"""
articulos = {
        0:{"marca":"Nike","modelo":"remera","color":"azul","precio":100,"cantidad":10}
    }

"""Metodo que guarda el inventario en un archivo .csv"""    
def guardarInventario():
    with open("datos.csv", "w") as datos:
        datos.write(str(articulos).strip())

"""Metodo que llama al archivo donde esta el inventario y muestra su contenido en pantalla"""
def verStock():
    with open('datos.csv') as file:
	    for line in file:
	        print(" ID: {}".format(line.strip().upper()))


"""Metodo que muestra la informacion de un articulo, ubicandolo por su ID"""
def verArticulo():
    msjnovalida = "********¡Tipo de Dato no valido!***********\n" 
    msjID = "Ingresar ID del Articulo a visualizar : "
    id = confirmacion(msjID)
    while not id.isdigit():
        print(msjnovalida)
        id = confirmacion(msjID)
    while int(id) not in articulos.keys():
        print("*****ID ingresado no exite*****")
        id = int(confirmacion(msjID))
    id = int(id)
    print("\nArticulo ID: {}".format(id))
    print("MARCA: {}".format(articulos[id]['marca']))
    print("MODELO: {}".format(articulos[id]['modelo']))
    print("COLOR: {}".format(articulos[id]['color']))
    print("PRECIO: {}$".format(articulos[id]['precio']))
    print("CANTIDAD DISPONIBLE: {}\n".format(articulos[id]['cantidad']))



