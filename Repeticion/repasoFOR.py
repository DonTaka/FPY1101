""" 
Gestionar las compras que realiza un cliente 
Pedir la cantidad de productos
Generar un ciclo for segun la cantidad de productos que el usuario requiere
Finalizar con un mensaje indicando 

Cantidad de compras 
Total sin iva 
Total con IVA
Controlar 2 errores por codigo y uno general
"""
print("Bienvenido")
try:
    total=0
    cantidadProductos = int(input("Cuantos productos desea: "))
    if(cantidadProductos>0):
        #Start = Inicio del ciclo
        #Stop = Fin del ciclo - 1
        #Step = El paso o avance del ciclo  
        #for i in range(Start:stop:step)
        for i in range(1,cantidadProductos+1):
            monto = 0
            while monto<=0:
                monto = int(input(f"Ingrese el monto del producto {i}: $"))
                if(monto>0):
                    total+=monto
                    print(f"Total actual: ${total}")
                else:
                    print("Debe ingresar un monto mayor a 0")
           
        totalConIVA = total*0.19
        totalConIVA = total+totalConIVA
        #totalConIVA = total*1.19
        print(f"Usted ha comprado un total de {cantidadProductos} productos")
        print(f"Total sin IVA: ${total}")
        print(f"Total con IVA: ${totalConIVA}")        
    else:
        print("Error: Debe ingresar una cantidad mayor a 0")       
except ValueError as error:
    print(f"Error: {error}")
    print("Error: Debe ingresar un valor numerico")
except TypeError as error:
    print(f"Error: {error}")
    print("Error: Tipo de dato erroneo")
except SyntaxError as error:
    print(f"Error: {error}")
    print("Error: Error de sintaxis , revisar el codigo")    
except:
    print("Error en el sistema ")
