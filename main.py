from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def main():
    mi_restaurante = Restaurante(nombre="Sabor Andino")

    plato1 = Producto(
        identificador=1,
        nombre="Encebollado",
        precio=5.75,
        es_bebida=False,
        disponibilidad=20
    )

    bebida1 = Producto(
        identificador=2,
        nombre="Jugo de naranja",
        precio=2.50,
        es_bebida=True,
        disponibilidad=30
    )

    cliente1 = Cliente(
        codigo=101,
        nombre="María López",
        correo="maria@correo.com",
        es_miembro=True
    )

    cliente2 = Cliente(
        codigo=102,
        nombre="Juan Pérez",
        correo="juan@correo.com",
        es_miembro=False
    )

    mi_restaurante.agregar_producto(plato1)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_cliente(cliente1)
    mi_restaurante.agregar_cliente(cliente2)

    print(f"=== Sistema de Gestión: {mi_restaurante.nombre} ===")
    mi_restaurante.mostrar_productos()
    mi_restaurante.mostrar_clientes()


if __name__ == "__main__":
    main()
