from tienda2 import Restaurante, Supermercado, Farmacia

# Función para crear una tienda segun lo seleccionado por el usuario
def crear_tienda():
    print("""
          
          Tipos de tienda disponibles:
          
          1.- Restaurante.
          2.- Supermercado.
          3.- Farmacia.
          
          """)
    tipo = int(input("Ingrese el tipo de tienda [1/2/3]: "))
    nombre = str(input("Ingrese el nombre de la tienda: "))
    costo_delivery = float(input("Ingrese el costo del delivery: "))
    
    # Retorna una instancia de la tienda correspondiente
    if tipo == 1:
        return Restaurante(nombre, costo_delivery)
    elif tipo == 2:
        return Supermercado(nombre, costo_delivery)
    elif tipo == 3:
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no valido")
        return None
    
# Función para ingresar productos a la tienda
def ingresar_productos(tienda):
    while True:
        nombre = input("\nIngrese el nombre del producto: ")
        precio = float(input("Ingrese el precio: "))
        stock = input("Ingrese el Stock: ")
        stock = int(stock) if stock else 0
        
        # Llama al método de la tienda para agregar el producto
        tienda.ingresar_producto(nombre, precio, stock)
        cont = input("\n¿Desea ingresar otro producto: [s/n]").strip().lower()
        if cont != "s":
            break
        
# Función principal de menú de opciones
def menu(tienda):
    while True:
        print("""
              
              Opciones disponibles.
              
              1.- Listar productos.
              2.- Realizar venta.
              3.- Salir
                           
              """)
        opcion = int(input("Seleccione una opcion: "))
        # Opción para listar productos
        if opcion == 1:
            print(tienda.listar_productos())
        # Opción para realizar una venta
        elif opcion == 2:
            nombre = input("Nombre del producto a vender: ")
            cantidad = int(input("Cantidad: "))
            tienda.realizar_venta(nombre, cantidad)
        # Opción para salir del programa
        elif opcion == 3:
            print("Hasta luego")
            break
        else:
            print("Opcion no valida")
        
# Punto de entrada principal del programa
if __name__ == "__main__":
    tienda = crear_tienda()
    if tienda:
        ingresar_productos(tienda)
        menu(tienda)
