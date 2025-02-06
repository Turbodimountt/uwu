print("Bienvenido a su cesta de la compra\n")

print("Elija una de las siguientes opciones:")

nombres = []
precios = []

while True:
    print("1. añadir articulo")
    print("2. ver articulos")
    print("3. remover articulos")
    print("4. suma total del carrito")
    print("5. salir")

    vainilla = input("Que eleccion deseas elegir:")

    if vainilla == "1":
        nombre = input("Introduzca el nombre del articulo:")
        precio = float(input(f"introduzca el precio del {nombre}: "))
        nombres.append(nombre)
        precios.append(precio)
        print(f"{nombre} se ha añadido al carrito \n")
    elif vainilla == "2":
        if len(nombre) == 0:
            print ("el carrito esta vacio")
        else:
            print("ver articulo:")
        for i in range(len(nombres)):
            print(f"{i+1}. {nombres[i]} - ${precios[i]}\n")
    elif vainilla == "3":
        if len(nombre) == 0:
            print("el carrito esta vacio")
        else:
            chocolate = int(input("que articulo desea eliminar?"))
            nombres.pop(chocolate-1)
            precios.pop(chocolate-1)
            print(f"articulo ha sido eliminado\n")
    elif vainilla =="4":
        total = sum(precios)
        print(f"el precio total de los articulos en el carrito es de ${total}\n")
    elif vainilla == "5":
        print("adios ,no vuela jamas. mala paga")
        break            


        