class Pila:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los elementos de la pila
        self.items = []

    def esta_vacia(self):
        # Devuelve True si la pila está vacía, False en caso contrario
        return self.items == []

    def insertar(self, item):
        # Inserta un nuevo elemento al final de la pila (tope de la pila)
        self.items.append(item)

    def eliminar(self, item):
        # Elimina el primer elemento que coincida con 'item' en la pila
        # Si el elemento no está presente, lanza una excepción ValueError
        if item in self.items:
            self.items.remove(item)
        else:
            raise ValueError("Elemento no encontrado en la pila")

    def buscar(self, item):
        # Devuelve True si el elemento 'item' se encuentra en la pila, False en caso contrario
        return item in self.items

# Ejemplo de uso:
pila = Pila()  # Crea una nueva instancia de la clase Pila
pila.insertar(1)  # Inserta el número 1 en la pila
pila.insertar(2)  # Inserta el número 2 en la pila
pila.insertar(3)  # Inserta el número 3 en la pila

try:
    pila.eliminar(3)  # Elimina el elemento 2 de la pila
except ValueError as e:
    print(e)  # Si ocurre un error al eliminar, lo imprime

print(pila.buscar(3))  # Verifica si el elemento 3 está en la pila, debería imprimir True

#El siguiente codigo realiza la estructura de datos de "PILA" (LIFO: Last In, First Out), el primero en entrar
#es el ultimo en salir, por lo cual se aplica al final de codigo y  realiza las acciones de (Inserción, Eliminacion y Busqueda)