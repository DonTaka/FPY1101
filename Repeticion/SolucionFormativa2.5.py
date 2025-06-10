#Menu Restaurant

#Menu de 5-6 opciones 
#Debe repetirse hasta que el usuario lo desee 
#Codigo debe ingresarse hasta que el usuario ingrese correctamente
#O desee volver
#Mostramos detalle y damos opcion a seguir comprando
#opt= option u opcion 
optGeneral = 0
print("Bienvenido a nuestro restaurante")
while optGeneral !=2:
    try:
        print("1.- Generar pedido")
        print("2.- Salir")
        optGeneral=int(input(""))
        if optGeneral==1:
            #Trabajamos todo el pedido
            contRollPika = 0
            contRollOta = 0
            contRollPulp = 0
            contRollAng = 0
            total = 0
            descuento = 0
            optPedido =0
            while optPedido!=6:
                print("Elija sus productos")
                print("1.- Pikachu Roll $4500")
                print("2.- Otaku Roll $5000")
                print("3.- Pulpo Roll $5200")
                print("4.- Anguila Roll $4800")
                print("5.- Aplicar descuento")
                print("6.- Salir")
                optPedido= int(input(""))
                match optPedido:
                    case 1:
                        contRollPika+=1
                        total+=4500
                    case 2:
                        contRollOta+=1
                        total+=5000
                    case 3:
                        contRollPulp+=1
                        total+=5200
                    case 4:
                        contRollAng+=1
                        total+=4800
                    case 5:
                        optCodigo=""
                        while optCodigo!=2:
                            print("Tiene un codigo de descuento")
                            print("1.- Si")
                            print("2.- No")
                            optCodigo = int(input(""))
                            if(optCodigo==1):
                                print("Si deseas volver al menu , ingresa X")
                                codigo=input("Ingrese su codigo: ")
                                if(codigo=="soyotaku"):
                                    descuento=total*0.10
                                    print("Descuento obtenido")
                                    break
                                elif(codigo=="X"):
                                    print("Volviendo al menu...")
                                    break
                                else:
                                    print("Codigo no valido")           
                    case 6:
                        totalconDescuento = total-descuento
                        print("--------------------")
                        cantidadTotal=contRollPika+contRollOta+contRollPulp+contRollAng
                        print(f"Total de productos: {cantidadTotal}")
                        print("--------------------")
                        print(f"Pikachu Roll: {contRollPika}")
                        print(f"Otaku Roll: {contRollOta}")
                        print(f"Pulpo Venenoso Roll: {contRollPulp}")
                        print(f"Anguila Roll: {contRollAng}")
                        print("----------------------")
                        print(f"Subtotal por pagar: ${total}")
                        print(f"Descuento aplicado: ${descuento}")
                        print(f"Total con descuento: ${totalconDescuento}")                       
                        
        else:
            print("Gracias por su preferencia")
    except:
        print("Ha sucedido un error")
