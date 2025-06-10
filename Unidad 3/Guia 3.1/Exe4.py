""" 
4)	Cree un menú para registrar usuarios e iniciar sesión, 
también el menú tendrá la opción de eliminar usuarios, 
para ello, utilice el nombre de usuario, 
además para confirmar la eliminación, 
deberán escribir la contraseña correspondiente de cada usuario.

1.	Inicio sesión.
2.	Registrar usuario
3.	Eliminar usuario.
4.	Salir.

La opción 1 sólo deberá mostrar un mensaje exitoso en caso de haber iniciado correctamente,
o un mensaje de error de caso contrario.
"""
usuarios = []
opcion = 0
while opcion!=4:
    print(usuarios)
    print("1.- Inicio Sesion")
    print("2.- Registrar Usuario")
    print("3.- Eliminar Usuario")
    print("4.- Salir")
    opcion = int(input(""))
    match opcion:
        case 1:
            
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            conexion = False
            for item in usuarios:
                if(item["username"]==username and item["password"]==password):
                    conexion = True
                    break
            if (conexion):
                print("Conexion exitosa")            
            else:
                print("Error en al conexion")
        case 2:
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            us = {
                "username":username,
                "password":password
            }
            usuarios.append(us)
            print("Agregado con exito")
        case 3:            
            username = input("Ingrese nombre de usuario: ")
            for item in usuarios:
                if item["username"]==username:
                    usuarios.remove(item)
                    print("Eliminado con exito")
                    break
        case 4:
            print("Gracias por su preferencia")
        case _:
            print("Opcion ingresada fuera de rango")
