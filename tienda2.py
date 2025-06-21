from abc import ABC, abstractmethod
from producto import Producto

# Clase abstracta base para las tiendas
class Tienda(ABC):
    def __init__(self, nombre: str, costo_delivery: float):
        # Nombre de la tienda (no modificable)
        self._nombre = nombre
        # Costo de delivery (no modificable)
        self._costo_delivery = costo_delivery
        # Lista de productos de la tienda
        self._productos = []
        
    # Propiedad para acceder al nombre de la tienda
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para acceder al costo de delivery
    @property
    def costo_delivery(self):
        return self._costo_delivery

    # Método para ingresar un producto a la tienda
    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo_producto = Producto(nombre, precio, stock)
        for i, prod in enumerate(self._productos):
            # Si el producto ya existe (por nombre), suma el stock
            if prod == nuevo_producto:
                self._productos[i] = prod + nuevo_producto
                return
        # Si es un producto nuevo, se agrega a la lista
        self._productos.append(nuevo_producto)

    # Método abstracto para listar productos (debe ser implementado por subclases)
    @abstractmethod
    def listar_productos(self) -> str:
        pass

    # Método abstracto para realizar una venta (debe ser implementado por subclases)
    @abstractmethod
    def realizar_venta(self, nombre_producto, cantidad):
        pass
        
# Clase para tiendas de tipo Restaurante
class Restaurante(Tienda):
    # Sobrescribe el método para ingresar productos: siempre stock 0
    def ingresar_producto(self, nombre, precio, stock=0):
        nuevo_producto = Producto(nombre, precio, 0)
        for i, prod in enumerate(self._productos):
            # Si el producto ya existe, no hace nada
            if prod == nuevo_producto:
                return
        self._productos.append(nuevo_producto)

    # Lista productos ocultando el stock
    def listar_productos(self) -> str:
        if not self._productos:
            return "No hay productos en el restaurante."
        # Solo muestra nombre y precio
        return "\n".join([f"{p.nombre} - ${p.precio}" for p in self._productos])

    # Realiza una venta (no valida stock)
    def realizar_venta(self, nombre_producto, cantidad):
        for prod in self._productos:
            if prod.nombre == nombre_producto:
                print(f"Venta realizada: {cantidad} x {prod.nombre}")
                return
        print("Producto no encontrado.")

# Clase para tiendas de tipo Supermercado
class Supermercado(Tienda):
    # Lista productos mostrando stock y advertencia si es bajo
    def listar_productos(self) -> str:
        if not self._productos:
            return "No hay productos en el supermercado."
        lineas = []
        for p in self._productos:
            mensaje = f"{p.nombre} - ${p.precio} - Stock: {p.stock}"
            # Mensaje especial si el stock es bajo
            if p.stock < 10:
                mensaje += " (Pocos productos disponibles)"
            lineas.append(mensaje)
        return "\n".join(lineas)

    # Realiza una venta validando stock
    def realizar_venta(self, nombre_producto, cantidad):
        for i, prod in enumerate(self._productos):
            if prod.nombre == nombre_producto:
                if prod.stock == 0:
                    print("No hay stock disponible.")
                    return
                # Vende solo lo que hay disponible si la cantidad es mayor al stock
                vendido = min(cantidad, prod.stock)
                self._productos[i].stock = prod.stock - vendido
                print(f"Venta realizada: {vendido} x {prod.nombre}")
                return
        print("Producto no encontrado.")
    
# Clase para tiendas de tipo Farmacia
class Farmacia(Tienda):
    # Lista productos ocultando stock y mostrando mensaje de envío gratis si corresponde
    def listar_productos(self) -> str:
        if not self._productos:
            return "No hay productos en la farmacia."
        lineas = []
        for p in self._productos:
            mensaje = f"{p.nombre} - ${p.precio}"
            # Mensaje especial si el precio es alto
            if p.precio > 15000:
                mensaje += " (Envío gratis al solicitar este producto)"
            lineas.append(mensaje)
        return "\n".join(lineas)

    # Realiza una venta validando stock y cantidad máxima por venta
    def realizar_venta(self, nombre_producto, cantidad):
        if cantidad > 3:
            print("No se puede vender más de 3 unidades por producto.")
            return
        for i, prod in enumerate(self._productos):
            if prod.nombre == nombre_producto:
                if prod.stock == 0:
                    print("No hay stock disponible.")
                    return
                # Vende solo lo que hay disponible si la cantidad es mayor al stock
                vendido = min(cantidad, prod.stock)
                self._productos[i].stock = prod.stock - vendido
                print(f"Venta realizada: {vendido} x {prod.nombre}")
                return
        print("Producto no encontrado.")