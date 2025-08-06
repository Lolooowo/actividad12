#def ordenamientoRepartidaores(lista):
repartidores ={}
numRepartidores = int(input("Ingrese el numero de repartidores: "))
for i in range(numRepartidores):
    nombre = input("Ingrese el nombre del repartidor: ")
    if nombre not in repartidores.keys():
        paquetes = int(input("Ingrese los paquetes entregados del repartidor: "))
        if paquetes < 0:
            print("No puede ingresar un numero negativo en paquetes")
        else:
            zona = input("Ingrese la zona del repartidor: ")
            if zona == "":
                print("No puede ingresar una zona vacia")
            else:
                repartidores[nombre] = {
                "paquetes": paquetes,
                "zona": zona
                }
    else:
        print("Ese nombre ya esta registrado")
