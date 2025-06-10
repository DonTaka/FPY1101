arancel =2200000
matricula=95000

promedio = float(input("Ingrese su promedio de notas: "))
decil = int(input("Ingrese su decil"))

if(promedio>6.5):
    match (decil):
        case 1:
            arancel*=0.75
            #arancel-=(arancel*0.25)
            #arancel-=(arancel*(25/100))
        case 2:
            arancel*=0.75
        case 3:
            arancel*=0.82
        case 4:
            arancel*=0.82
        case _:
            print("No posee descuento")
elif (promedio>=5.5 and promedio<=6.5):
    match (decil):
        case 1:
            arancel*=0.85
        case 2:
            arancel*=0.85
        case 3:
            arancel*=0.88
        case 4:
            arancel*=0.88
        case _:
            print("No posee descuento")
else:
    print("No posee descuento de arancel")
#Forma 1 
""" if(decil>=1 and decil<=3):
    matricula*=0.88
    if(promedio>=6):
        matricula*=0.95 """
#Forma 2
descuento = 0

if(decil>=1 and decil<=3):
    descuento= (matricula*0.12)
    if(promedio>=6):
        descuento = matricula*0.17
matricula-=descuento
print(f"Arancel: ${arancel}")
print(f"Matricula: ${matricula}")
            