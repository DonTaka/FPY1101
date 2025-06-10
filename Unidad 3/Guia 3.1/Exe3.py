""" 
3)	Cree una lista y comience a almacenar nombres, 
cada vez que se agregue un nombre nuevo, 
el sistema preguntará si desea agregar otro nombre, 
deberá agregar nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” 
(use funciones lower() y upper() ) .
Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres.
"""
nombres = []
respuesta = "si"

while respuesta=="si":
    nombre = input("Ingrese su nombre: ")
    nombres.append(nombre)
    print("Desea agregar otro nombre? (Si o No)")
    respuesta = input("").lower()
print(nombres)

menor = ""

for item in nombres:
    if menor.__len__()==0:
        menor = item
    if item.__len__()<menor.__len__():
        menor = item
nombres.remove(menor)

print(nombres)
    