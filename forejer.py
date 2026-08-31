import os 
def ventasminisuper():
    os.system("cls")
    # Registra las ventas de lunes a domingo. 
    # Calcula el total semanal y el promedio diario.
    total = 0 
    for i in range(7):
        venta = int(input(f"Ingrese la venta del día {i + 1 }: "))
        total += venta
    promedio = total / 7 

    print(f"El totla semanal es: {total}")
    print(f"El promedio diario es: {promedio}")
    print("")


def Recepcióncafé():
    os.system("cls")
    #Una cooperativa recibe 5 sacos.
    # Solicita el peso de cada uno,
    # muestra su número de recepción y calcula el peso total.
    i=0
    pesoTotal = 0
    for i in range(5):
        peso = int(input(f"Ingrese el peso del saco #{i + 1}: "))
        pesoTotal += peso
    print(f"El peso total es: {pesoTotal}")


def Revisióninventario(): #falta imprimir los q tienen menos de 10 uhhhhhh
    os.system("cls")
    #Una distribuidora revisa 8 productos.
    #Solicita nombre y existencia; 
    #muestra los que tienen menos de 10 unidades y cuenta las alertas.
    alerta = 0
    for i in range(8):
        nombreproducto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese la cantidad existente: ")) 
        if unidades < 10:
            print(f"¡Oh no! el producto '{nombreproducto}' tiene menos de 10 unidades...")
            alerta += 1
        else: 
            break

    print (f"Cantidad de alertas:{alerta}")
    

def Producciónpan():
    os.system("cls")
    # Una panadería registra durante 6 días la producción y las ventas.
    # Calcula totales y producto sobrante.
    totalProduccion = 0
    totalVentas = 0
    for i in range(6):
        print(f"Día #{i+1}")
        produccion = int(input(f"Ingrese la producción del día: "))
        ventas = int(input("Ingrese las ventas del día: "))
        
        totalProduccion += produccion
        totalVentas += ventas

    sobrante = totalProduccion - totalVentas

    print(f"Producción total: {totalProduccion}")
    print(f"Ventas totales: {totalVentas}")
    print(f"Productos sobrante: {sobrante}")

    
def Evaluaciónservicio():
    os.system("cls")
    #Un restaurante recoge 10 calificaciones entre 1 y 5.
    # Calcula el promedio y cuenta cuántas fueron 4 o 5.
    total = 0
    califbuenas = 0

    for i in range(10):
        print(f"Calificación #{i+1}")
        calificacion = int(input("Ingrese una calificacion de 1 a 5: "))
        total += calificacion

        if calificacion == 4 or calificacion == 5:
            califbuenas += 1

    promedio = total / 10

    print(f"El promedio es: {promedio}")
    print(f"Cantidad de calificaciones de 4 o 5: {califbuenas}")
