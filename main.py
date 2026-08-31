import os
from forejer import ventasminisuper, Recepcióncafé, Revisióninventario, Producciónpan, Evaluaciónservicio
from whileejer import Cierrecaja, Accesosistema, Cantidadpedido, Combustiblereparto, Reposiciónexistencias

def main():
    os.system("cls")
    print("*********** MENU DE LOS EJERCICIOS ***********")
    print("********** Ejercicios de bucles for **********")
    print("1.......................Ventas de un minisúper")
    print("2............................Recepción de café")
    print("3.......................Revisión de inventario")
    print("4............................Producción de pan")
    print("5......................Evaluación del servicio")
    print("********* Ejercicios de bucles while *********")
    print("6...............................Cierre de caja")
    print("7............................Acceso al sistema")
    print("8........................Cantidad de un pedido")
    print("9.......................Combustible de reparto")
    print("10...................Reposición de existencias")
    opc = int(input("Seleccione la tarea a ejecutarse: "))
    match opc:
        case 1:
            ventasminisuper()
        case 2:
            Recepcióncafé()
        case 3: 
            Revisióninventario()
        case 4:
            Producciónpan()
        case 5:
            Evaluaciónservicio()
        case 6:
            Cierrecaja()
        case 7:
            Accesosistema()
        case 8:
            Cantidadpedido()
        case 9:
            Combustiblereparto()
        case 10:
            Reposiciónexistencias()


main()


