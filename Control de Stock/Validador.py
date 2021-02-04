from Mensajes import *
from MenuPpl import *
from Inventario import *

"""Metodo que toma un mensaje que le pasemos, lo muesta en pantalla y pide un tipo de dato """
def ingresarOpcion(msj):
    opcion = input(msj)
    res = validarN(opcion, msj)
    return res

"""Metodo que valida que el tipo de dato ingresado sea numerico"""
def validarN(option, msj):
    msjnovalida = "********¡Tipo de Dato no valido!***********" 
    while not option.isdigit():
        print(msjnovalida)
        option = input(msj)
    return option

"""Metodo que valida que la opcion ingresada sea alguna de las que muestra el menu"""    
def validarMenu(option, msj, menu):
    msjnovalida = "\n********¡Opción no encontrada!***********\n" 
    while not option.isdigit() or (int(option) not in menu.keys()):
        for o in menu:
            print(o ,"-", menu[o],"\n")
        print(msjnovalida)
        option = input(msj)
    return option  




   
"""Metodo que solicita confirmacion del dato ingresado"""
def confirmacion(msj):
    print("")
    op = input(msj)
    print("\n Ingresaste: ", op)
    conf = input("¿Es Correcto? (Y/n): ")
    while (conf != "y" and conf != "Y" and conf != ""):
        op = input(msj)
        print("\nIngresaste: ", op)
        conf = input("Es Correcto? (Y/n): ")
    return op





"""Metodo que consulta antes de finalizar el programa, si se desea realizar alguna otra operacion dentro del sistema""" 
def repetirOperacion():
    print("")
    conf = input("¿Deseas realizar otra operación? (y/N): ")
    while conf != "y" and conf != "Y" and conf != "n" and conf != "N" and conf != "":
         print("Opcion no valida")
         conf = input("¿Deseas realizar otra operación? (y/N): ")

    return conf
    
