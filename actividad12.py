def ordenamientoRepartidaores(lista):
    if len(lista)<=1:
        return lista
    else:
        pivote = lista[nombre]["paquetes"]
        mayores = [value for value in lista[1:].values("paquetes") if value > pivote]
        iguales = [value for value in lista.values() if value==pivote]
        menores = [value for value in lista[1:].values("paquetes") if value < pivote]
        return ordenamientoRepartidaores(mayores) + iguales + ordenamientoRepartidaores(menores)
def buscarRepartidor(lista, objetivo):
    for clave, valor in lista.items():
        if clave == objetivo:
            return clave
    else:
        return None
def cantidadPaquetes(repartidores):
    pedidos =0
    for clave, valor in repartidores.items():





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
ordenados = ordenamientoRepartidaores(repartidores)
print(ordenados)

nombreBuscar = input("Ingrese el nombre de un repartidor para buscarlo: ")
for clave, valor in repartidores.items():
    if clave == nombreBuscar:
        print(f"{clave}: paquetes entregados: {valor['paquetes']} ")
