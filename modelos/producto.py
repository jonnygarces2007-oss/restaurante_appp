class Producto:
    """Clase que representa un producto disponible en el restaurante"""

    def __init__(self, identificador: int, nombre: str, precio: float, es_bebida: bool, disponibilidad: int):
        # Atributos con tipos de datos claros
        self.identificador = identificador       # Número único de identificación
        self.nombre = nombre                      # Nombre del plato o bebida
        self.precio = precio                      # Valor en dólares
        self.es_bebida = es_bebida                # True si es bebida, False si es comida
        self.disponibilidad = disponibilidad      # Cantidad disponible en inventario

    def __str__(self) -> str:
        """Representación en texto del objeto Producto"""
        tipo = "Bebida" if self.es_bebida else "Comida"
        return (f"ID: {self.identificador} | Nombre: {self.nombre} | Tipo: {tipo} | "
                f"Precio: ${self.precio:.2f} | Disponibles: {self.disponibilidad}")
