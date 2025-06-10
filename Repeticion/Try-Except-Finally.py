

#TRY-EXCEPT-FINALLY

num = 1 


valor = 10/0
print(valor)

while num>0:
    try:
        num = int(input("Ingrese un numero :"))
    except IndexError:
        print("Debe ingresar un numero")
    except ZeroDivisionError:
        print(0)
    else:
        #Si salio todo bien 
        print(num)
    finally:
        #Ejecucion que cierra este bien o este mal 
        print("Gracias por su preferencia")    
    
