import os
def Cierrecaja():
    os.system("cls")
    #Ingresa los montos de ventas hasta escribir 0.
    # Calcula el total recaudado y la cantidad de ventas.
    total= 0
    ventas = 0
    print("--Si desea salir ingrese 0--")
    venta = int(input("Ingrese la cantidad a vender: "))
    while venta != 0:
        total += venta
        ventas += 1
        venta = int(input("Ingrese la cantidad a vender: "))
    print(f"El total recaudado es igual a: {total}")
    print(f"La cantidad de ventas fue: {ventas}")

def Accesosistema():
    os.system("cls")
    #Solicita la clave hasta que sea correcta. 
    #Cuenta los intentos e informa cuántos fueron necesarios.
    #La contra es conejoarcoiris

    intentos = 0
    contra = input("Por favor ingresa la contraseña para acceder al sistema: ")
    while contra != "conejoarcoiris":
        print("¡Contraseña incorrecta!")
        intentos += 1
        contra = input("Por favor ingresa la contraseña para acceder al sistema: ")

    print("¡Contraseña correcta!")
    print(f"Se necesitaron {intentos + 1} intentos.")




def Cantidadpedido():
    os.system("cls")
    #Un distribuidor acepta de 1 a 100 unidades. 
    #Solicita la cantidad hasta que sea válida y luego calcula el total.
    cantidad = int(input("Ingresa la cantiad de unidades que deseas: "))
    while cantidad < 1 or cantidad > 100:
        print("Cantidad inválida. Debe estar entre 1 y 100")
        cantidad = int(input("Ingresa la cantiad de unidades que deseas: "))

    print(f"El total es igual a {cantidad * 30} córdobas")
    

def Combustiblereparto():
    os.system("cls")
    #Una motocicleta inicia con 8 litros. 
    #Registra el consumo de cada recorrido
    #mientras quede combustible y alerta al llegar a 1 litro.
    consumo = 8
    gasolina = int(input("Ingrese cuanta gasolina consumio: "))
    while consumo  > 1:
        consumo -=  gasolina
        if consumo  > 1 and consumo <8:
          gasolina = int(input("Ingrese cuanta gasolina consumio: "))
        
        if consumo < 1:
            print("Uhh... Se quedo sin gasolina :c")
            break
        if consumo == 1:
            print("¡Alerta! se esta quedando sin gasolina, solo queda 1 litro")

    


    

def Reposiciónexistencias():
    os.system("cls")
    #Una tienda tiene 3 unidades y desea llegar a 20.
    #Solicita cada reposición y termina al alcanzar o superar la meta.
    unidades = 3
    
    while unidades < 20:
        reposicion  = int(input("Ingrese la cantidad a reponer: "))
        unidades += reposicion
    print(f"La tienda ahora tiene {unidades} unidades")
        

