suma = 0
costo =0 
try:
    pasajes = int(input("Ingrese cuantos pasajes desea: "))
    if(pasajes>0):
        for i in range(pasajes):
            costo = int(input("Cual es el valor de su pasaje? "))
            if(costo>0):
                suma+=costo
            else:
                print("Debe ingresar un monto mayor a 0")
                #Al leer break , la iteracion tiene la orden de detener su flujo de repeticion.
                break
        print(f"Usted compro un total de {pasajes} pasajes")
        print(f"Debe pagar un total de ${suma}")    
    else:
        print("Debe ingresar un numero mayor a 0")
except ValueError as error:
    print(f"Error: {error}")
    