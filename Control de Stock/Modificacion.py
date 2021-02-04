from Inventario import *
from Validador import *

""""Metodo que valida que la opcion ingresada este dentro de las disponibles en el sistema"""
def valorN(op):
    print("***Opcion no encontrada***")
    op = ingresarOpcion("Seleccione el campo a modificar : ")
    return op

"""Metodo que se encarga de validad y realizar la modificacion de algun articulo seleccionado y disponible en el sistema
muestra los campos que podemos modificar y una vez seleccionado, actuliza la informacion en el inventario"""
def modificarArt():
    msjnovalida = "********¡Tipo de Dato no valido!***********\n" 

    msjID = "Ingresar ID del Articulo a Modificar : "
    idArt = confirmacion(msjID)
    while not idArt.isdigit():
        print(msjnovalida)
        idArt = confirmacion(msjID)

    while int(idArt) not in articulos.keys():
        print("*****ID ingresado no existe*****")
        idArt = confirmacion(msjID)


    j = 1
    for i in articulos[0].keys():
        print("\n{} - {}\n".format(j, i.upper()))
        j += 1

    opMod = int(ingresarOpcion("Seleccione el campo a modificar : "))
    

    while opMod > len(articulos[0].keys()) or opMod < 1:
        opMod = int(valorN(opMod))
    if opMod == 1:
        msjMarca = "Ingrese Marca del Articulo: "
        marca = confirmacion(msjMarca)
        articulos[int(idArt)]["marca"] = marca
    elif opMod == 2:
        msjModelo = "Ingrese Modelo del Articulo: "
        modelo = confirmacion(msjModelo)
        articulos[int(idArt)]["modelo"] = modelo
    elif opMod == 3:
        msjColor = "Ingrese Color del Articulo: "
        color = confirmacion(msjColor)
        articulos[int(idArt)]["color"] = color
    elif opMod == 4:
        msjPrecio = "Ingrese Precio del Articulo: " 
        precio = confirmacion(msjPrecio)
        while not precio.isdigit():
            print(msjnovalida)
            precio = confirmacion(msjPrecio)
        articulos[int(idArt)]["precio"] = precio
    elif opMod == 5:
        msjCantidad = "Ingresar cantidad de Articulos: "
        cantidad = confirmacion(msjCantidad)
        while not cantidad.isdigit():
            print(msjnovalida)
            cantidad = confirmacion(msjCantidad)
        articulos[int(idArt)]["cantidad"] = cantidad
    

