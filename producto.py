class Producto:
    # Constructor de la clase Producto
    def __init__(self, nombre: str, precio: float, stock: int = 0):
        
        # Atributos privados para encapsulamiento
        self._nombre = nombre
        self._precio = precio
        
        # El stock no puede ser menor a 0
        self._stock = max(0, stock)

    # Propiedad para acceder al nombre (solo lectura)
    @property
    def nombre(self):
        return self._nombre

    # Propiedad para acceder al precio (solo lectura)
    @property
    def precio(self):
        return self._precio

    # Propiedad para acceder al stock (lectura y escritura)
    @property
    def stock(self):
        return self._stock

    # Setter para modificar el stock, nunca menor a 0
    @stock.setter
    def stock(self, valor):
        self._stock = max(0, valor)

    # Sobrecarga del operador == para comparar productos por nombre
    def __eq__(self, other):
        if isinstance(other, Producto):
            return self.nombre == other.nombre
        return False

    # Sobrecarga del operador + para sumar stock de productos con el mismo nombre
    def __add__(self, other):
        if isinstance(other, Producto) and self == other:
            nuevo_stock = self.stock + other.stock
            return Producto(self.nombre, self.precio, nuevo_stock)
        raise ValueError("Solo se pueden sumar productos con el mismo nombre.")

    # Sobrecarga del operador - para restar stock, nunca menor a 0
    def __sub__(self, cantidad):
        if isinstance(cantidad, int):
            nuevo_stock = max(0, self.stock - cantidad)
            return Producto(self.nombre, self.precio, nuevo_stock)
        raise ValueError("Solo se puede restar una cantidad entera al stock.")
