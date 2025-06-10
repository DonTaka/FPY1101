deuda = 100000
opcion = 0 

while opcion!=3:
    try:
        print("Bienvenido al sistema de gestion de credito")
        print("1.- Pagar tarjeta")
        print("2.- Comprar producto")
        print("3.- Salir")
        
        opcion =int(input("Que opcion desea: "))
        match (opcion):
            case 1:
                #Caso 1
                monto = int(input("Ingrese monto que desea abonar de la deuda: "))
                if(monto>0):
                    if(monto<=deuda):
                        deuda-=monto
                        print(f"Su deuda actual es de ${deuda}")
                    else:
                        print(f"Solo puede abonar como maximo su deuda actual ${deuda}")
                else:
                    print("Debe ingresar un monto mayor a 0")
            case 2:
                #Caso 2
                optCompra =0
                while optCompra!=2:
                    print("Desea comprar producto? ")
                    print("1.- Si")
                    print("2.- No")
                    optCompra = int(input(""))
                    if(optCompra==1):
                        compra = int(input("Indique monto de la compra: "))
                        deuda+=compra
                        print(f"Su deuda actual es de: ${deuda}")                    
            case 3:
                print("Gracias por su preferencia")
                #Caso 3
            case _:
                print("Opcion fuera de rango")
                #Caso fuera de rango
                
    except ValueError as err:
        print(f"Error Message: {err}")
    except:
        print("Ha surgido un error en el sistema")
        