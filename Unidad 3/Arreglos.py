#Arreglos
# Arreglo = [] || Brackets

arreglo = [1,"Jose",3.14,True] #<-- esto es un arreglo 
#Append = Agrega un nuevo elemento a la lista
arreglo.append(5)
print(f"Ejemplo append: {arreglo}")
#insert = Entregamos indice mas valor y agrega en la posicion
arreglo.insert(1,2)
print(f"Ejemplo insert: {arreglo}")
#remove = entregamos un valor ,busca y elimina
#Si funciona , todo OK , si no , lanza un error
#Revisar porque True toma el primer elemento 
try:        
    arreglo.remove(5)
    print(f"Ejemplo remove: {arreglo}")
except ValueError as error:
    #print(f"Ha sucedido un error: {error}")
    print("Elemento no existe en la lista")

#Reverse = Invierte el orden de la lista
#sort = Reordena la lista de menor a mayor
#arreglo.reverse()
print(f"Ejemplo reverse: {arreglo}")
try:
    arreglo.sort()
    print(f"Ejemplo sort: {arreglo}")
except TypeError as error:
    print(f"Ha sucedido un error: {error}")
    print("Para usar sort , deben ser valores numericos")
    
#Forma 1 : For con indice
#__len__ : Entrega el largo numerico del arreglo(Cuantos elementos tiene)
largo = arreglo.__len__()
print("For con indice")
for i in range(largo):
    print(arreglo[i])
    
#forma : formato foreach
print("Foreach")
for item in arreglo:
    print(item)
