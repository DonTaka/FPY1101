""" 
2)	Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos 
    (1 lista para nombres y una 1 lista para apellidos), 
    el sistema deberá mostrar de forma ordenada los nombres y apellidos.
"""
nombres = ["Jose","Sol","Fernando"]
apellidos = ["Riquelme","Escobar","Torres"]

nombres.sort()
apellidos.sort()
#Aca mostramos el arreglo completo
print(nombres)
#Aca mostramos uno por uno 
for item in apellidos:
    print(item)