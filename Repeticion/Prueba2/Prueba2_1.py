quintil = int(input("Ingrese su quintil: "))
condicion = input("Ingrese su condicion de empleabilidad: ")
bono = 0
if condicion.lower()=="empleado":
    match (quintil):        
        case 1:
            bono =300000
        case 2:
            bono =300000
        case 3:
            bono =150000
        case 4:
            bono = 0
        case 5:
            bono = 0
        case _:
            print("Debe ingresar un quintil entre 1-5")
                
    edad = int(input("Ingrese su edad: "))
    if(edad>60):
        bono+=30000
    print(f"Condicion laboral: {condicion}")
    print(f"Edad: {edad}")
    print(f"Quintil: {quintil}")
    print(f"Bono total: {bono}")
elif condicion.lower()=="desempleado":    
    match (quintil):        
        case 1:
            bono =350000
        case 2:
            bono =350000
        case 3:
            bono =200000
        case 4:
            bono = 0
        case 5:
            bono = 0
        case _:
            print("Debe ingresar un quintil entre 1-5")    
    edad = int(input("Ingrese su edad: "))
    if(edad>60):
        bono+=30000
    print(f"Condicion laboral: {condicion}")
    print(f"Edad: {edad}")
    print(f"Quintil: {quintil}")
    print(f"Bono total: {bono}")
else:
    print("Debe ingresar Empleado o desempleado")


    
        
        