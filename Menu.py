from Cajero import Cajero

salir = False
cajero_opciones = Cajero()

while not salir:
    print("=== SISTEMA CAJERO ===")
    print("1. Crear mesa")
    print("2. Agregar pedido")
    print("3. Cobrar mesa")
    print("4. Resumen del dia")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        numero_mesa = int(input("Ingrese numero de la mesa que desea crear "))
        cajero_opciones.crear_mesa(numero_mesa)
    elif opcion == "2":
        numero_mesa = int(input("Ingrese el numero de la mesa que desea agregar el pedido: "))
        comida = input("Ingrese el pedido: ")
        precio = float(input("Ingrese el precio del pedido"))
        cajero_opciones.registrar_pedido_en_mesa(numero_mesa, comida, precio)
    elif opcion == "3":
        numero_mesa = int(input("Ingrese el numero de la mesa que desea cobrar el pedido: "))
        dinero_cliente = float(input("Ingrese el dinero que dio el cliente: "))
        cajero_opciones.cobrar_mesa(numero_mesa,dinero_cliente)
    elif opcion == "4":
        cajero_opciones.resumen_dia()
    elif opcion == "5":
        print("Saliendo del sistema")
        salir = True
    else:
        print("Escoja una opcion del rango permitido")