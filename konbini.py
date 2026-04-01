
#Base  de datos de la konbini
Productos = ["Manzana", "Pera", "Uva", "Platano", "Sandia", "Naranja", "Limon", "Kiwi", "Piña", 
"Mango", "Frutilla", "Arandano", "Cereza", "Melon", "Durazno", "Damasco", "Ciruela", "Higo", "Frambuesa", "Mora"]
Precios = [1200, 800, 1500, 600, 3500, 900, 500, 1100, 2200, 1800, 2500, 3000, 4500, 2800, 1300, 1400, 1100, 1900, 3200, 2700]
Ventas = []
#######################################################################################################################################

while True:
    user = str(input("ingrese su usuario: "))
    password = str(input("ingrese su contraseña: "))

    if user != "admin" or password != "udp.2026":
        print("Usuario o contraseña incorrectos (reintente)")
    else:
        print("--------------------------------------------Bienvenido al sistema de ventas de la konbini---------------------------------------------")
        while True:
            print(f"Que operacion desea realizar {user}?")
            print("1. Agregar producto")
            print("2. Eliminar producto")
            print("3. Modificar precio de producto")
            print("4. Mostrar productos")
            print("5. Realizar venta")
            print("6. Ver ventas realizadas")
            print("7. Salir")

            opcion = int(input("Ingrese el numero de la operacion que desea realizar: "))

            if opcion == 1:
                nuevo_producto = str(input("Ingrese el nombre del nuevo producto: "))
                nuevo_precio = int(input("Ingrese el precio del nuevo producto: "))
                Productos.append(nuevo_producto)
                Precios.append(nuevo_precio)
                print(f"Producto {nuevo_producto} agregado con precio {nuevo_precio}")
            elif opcion == 2:
                producto_eliminar = str(input("Ingrese el nombre del producto que desea eliminar: "))
                if producto_eliminar in Productos:
                    i = Productos.index(producto_eliminar)
                    Productos.pop(i)
                    Precios.pop(i)
                    print(f"Producto {producto_eliminar} eliminado")
                else:
                    print("Producto no encontrado")
            elif opcion == 3:
                producto_modificar = str(input("Ingrese el nombre del producto que desea modificar: "))
                if producto_modificar in Productos:
                    i = Productos.index(producto_modificar)
                    nuevo_precio = int(input("Ingrese el nuevo precio del producto: "))
                    Precios[i] = nuevo_precio
                    print(f"Precio del producto {producto_modificar} modificado a {nuevo_precio}")
                else:
                    print("Producto no encontrado")
            elif opcion == 4:
                print("Productos disponibles:")
                for i in range(len(Productos)):
                    print(f"{Productos[i]}: {Precios[i]} pesos")
            elif opcion == 5:
                boleta = []
                while True:
                    producto_venta = str(input("Ingrese el nombre del producto que desea vender (o 'salir' para finalizar la venta): "))
                    if producto_venta == "salir":
                        if len(boleta) > 0:
                            for i in range(len(boleta)):
                                print(f"Producto {i+1}: {boleta[i]} pesos")
                            print(f"Total a pagar: {sum(boleta)} pesos")
                            Ventas.append(sum(boleta))
                            print(f"Venta realizada por un total de {sum(boleta)} pesos")
                            break
                        else:
                            print("No se ha realizado ninguna venta")
                        break
                    else:
                        if producto_venta in Productos:
                            qty = int(input(f"Ingrese la cantidad de {producto_venta} que desea vender: "))
                            i = Productos.index(producto_venta)
                            total = Precios[i] * qty
                            boleta.append(total)
                        else:
                            print("Producto no encontrado")
            elif opcion == 6:
                if len(Ventas) > 0:
                    print("Ventas realizadas:")
                    for i in range(len(Ventas)):
                        print(f"Venta {i+1}: {Ventas[i]} pesos")
                else:
                    print("No se han realizado ventas")
            elif opcion == 7:
                print("Saliendo del sistema de ventas de la konbini")
                break
            else:
                print("Opcion no valida, por favor ingrese un numero del 1 al 7")

    break

