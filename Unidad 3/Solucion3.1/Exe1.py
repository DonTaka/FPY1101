""" 
1)	Escriba un programa que permita almacenar 3 nombres solicitados por pantalla 
    en una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres 
    en un mensaje de salida por pantalla.
"""
nombres = []

for i in range(3):
    nombre = input("Ingrese su nombre: ")
    if(nombre.__len__()>0):
        nombres.append(nombre)
    else:
        print("Debe ingresar mas caracteres")

palabraMayor = ""

for item in nombres:
    if item.__len__()>palabraMayor.__len__():
        palabraMayor = item
        
print(f"El nombre con mayor cantidad de letras es {palabraMayor}") 