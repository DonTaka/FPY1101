""" 
3)	Cree una lista y comience a almacenar nombres, 
cada vez que se agregue un nombre nuevo, 
el sistema preguntará si desea agregar otro nombre, 
deberá agregar nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” 
(use funciones lower() y upper() ) .
Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres.
"""

nombres = []
opcion = "si"
while opcion == "si":
    nombre = input("Ingrese nombre: ")
    nombres.append(nombre)
    print("Desea agregar mas nombres")
    opcion = input("Si/No").lower()

nombreMenor = ""

print(nombres)
for item in nombres:   
    print(f"Nombre actual tiene {len(item)} letras") 
    if(nombreMenor.__len__()==0):
        nombreMenor=item
       
    if(item.__len__()<nombreMenor.__len__()):
        nombreMenor= item
        
print(f"Nombre: {nombreMenor} sera eliminado")
nombres.remove(nombreMenor)
print(nombres)
        
