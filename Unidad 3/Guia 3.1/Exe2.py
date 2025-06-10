""" 
2)	Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos 
    (1 lista para nombres y una 1 lista para apellidos), 
    el sistema deberá mostrar de forma ordenada los nombres y apellidos.
"""
nombres = ["Ignacio","Luna","Fernando"]
apellidos = ["Riquelme","Escobar","Jara"]

nombres.sort()
apellidos.sort()
#Sort en texto ordena por la primera letra 
for item in nombres:
    print(item)
for item in apellidos:
    print(item)