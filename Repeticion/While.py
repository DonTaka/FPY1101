
#While
#Ciclo se repite mientras la condicion sea verdadera 

opcion = 1
#MIENTRAS LA CONDICION SEA VERDADERA , REPITE INFINITAMENTE
#SI ES FALSA , EL CICLO TERMINA
while opcion!=4:
    print("Bienvenido")
    print("1.- Opcion 1")
    print("2.- Opcion 2")
    print("3.- Opcion 3")
    print("4.- Salir")
    opcion = int(input("Ingrese la opcion que desea: "))
    
    match opcion:
        case 1:
            print("Eligio la opcion 1")
        case 2:
            print("Eligio la opcion 2")
        case 3:            
            print("Eligio la opcion 3")
        case 4:
            print("Gracias por su preferencia")
        case _:
            print("Error, Debe ingresar una opcion entre 1 y 4 ")
    