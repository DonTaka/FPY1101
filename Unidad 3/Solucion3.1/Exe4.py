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
    print("Bienvenido Usuario ")
    print("1.- Iniciar Sesion")
    print("2.- Registrar Usuario")
    print("3.- Eliminar Usuario")
    print("4.- Salir")
    opcion = int(input(""))
    match opcion:
        case 1:
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            conectado = False
            for item in usuarios:
                if(item["username"]==username and item["password"]==password):
                    conectado=True
            if(conectado):
                print("Ha conectado con exito")
            else:
                print("Error en las credenciales ")
        case 2:
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            usuario = {
                "username":username,
                "password":password
            }
            usuarios.append(usuario)
            print("Usuario agregado con exito")
        case 3:
            username = input("Ingrese su nombre de usuario: ")
            for item in usuarios:
                if(item['username']==username):
                    usuarios.remove(item)
                    print(f"Usuario: {username} eliminado")
                    break
                    
            
        case 4:
            print("Gracias por su preferencia")
        case _:
            print("Opcion fuera de rango")
            
    