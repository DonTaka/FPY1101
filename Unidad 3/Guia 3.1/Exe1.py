""" 
1)	Escriba un programa que permita almacenar 3 nombres solicitados por pantalla 
    en una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres 
    en un mensaje de salida por pantalla.
"""
nombres = ["Jose","Luna","Fernando"]

mayor = ""

for item in nombres:
    if item.__len__()>mayor.__len__():
        mayor = item

print(mayor)
