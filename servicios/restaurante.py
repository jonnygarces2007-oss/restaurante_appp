from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:

    def __init__(self, nombre: str):
        self.nombre = nombre                         # Nombre del restaurante
        self.lista_productos: List[Producto] = []   # Lista para almacenar objetos Producto
        self.lista_clientes: List[Cliente] = []      # Lista para almacenar objetos Cliente

    def agregar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    def mostrar_productos(self) -> None:
        print("\n--- Menú de Productos ---")
        if not self.lista_productos:
            print("No hay productos registrados.")
            return
        for producto in self.lista_productos:
            print(producto)

    def mostrar_clientes(self) -> None:
        print("\n--- Lista de Clientes ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return
        for cliente in self.lista_clientes:
            print(cliente)
