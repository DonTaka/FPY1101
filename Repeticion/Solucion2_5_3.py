""" 
deuda inicial = 100k
1.- Menu de 3 opciones 
2.- Primera opcion pagar deuda
3.- Segunda opcion comprar ilimitadamente
4.- Tercera opcion Salir
5.- Validar control de errores con 3 excepciones minimo
"""
deuda = 100000
opcion = 0
while opcion!=3:
    try:
        print("Bienvenido al servicio de tarjeta de credito")
        print("1.- Pagar deuda actual")
        print("2.- Comprar producto")
        print("3.- Salir")
        opcion=int(input(""))
        match opcion:
            case 1:
                monto = int(input("Ingrese monto que desea pagar: $"))
                #Monto mayor a 0
                if (monto>=0):
                    #Monto no puede ser mayor a la deuda
                    if(monto<=deuda):
                        deuda-=monto
                        print(f"Usted ha pagado un total de ${monto}")
                        print(f"Deuda actual registrada: ${deuda}")
                    else:
                        print("No puede pagar un monto mayor al de su deuda")
                else:
                    print("Debe ingresar un monto mayor a 0")
            
            case 2:
                #Comprar
                optCompra=0
                monto=0
                while optCompra!=2:
                    print("1.- Ingresar monto compra")
                    print("2.- Terminar compra")
                    optCompra = int(input("Ingrese opcion: "))
                    if (optCompra==1):
                        #Desea comprar
                        monto += int(input("Ingrese monto de la compra: $"))                        
                    elif(optCompra==2):
                        print(f"Ha comprado un total de ${monto}")
                        deuda+=monto
                        print(f"Su deuda actual es: ${deuda}")
                    else:
                        print("Debe ingresar opcion 1 o 2")
            case 3:
                #Salir
                print("Gracias por su preferencia :3")
            case _:
                #Cualquier valor menos 1-2-3
                print("Ha ingresado un valor fuera de rango")
    except ValueError as error:
        print(f"Ha sucedido un error: {error}")
    except NameError as error:
        print(f"Ha sucedido un error: {error}")
    except:
        print("Ha sucedido un error: Undefined")