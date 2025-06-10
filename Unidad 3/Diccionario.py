#Diccionarios
#Diccionario trabaja similar a un arreglo pero su identificador es textual

diccionario ={
    "Nombre":"",
    "Edad":29,
    "Rut":19142423-9,
    "Cargo":"Docente",
    "Secciones":["004D","005D","007D","008D","009D"]
}

#pop(x) = Eliminar segun posicion(arreglos) o llaves(Diccionario)
diccionario.pop("Secciones")
print(diccionario.items())

nombre = input("Ingrese su nombre: ")
diccionario["Nombre"]=nombre;
print(diccionario.items())