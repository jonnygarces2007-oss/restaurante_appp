class Cliente:

    def __init__(self, codigo: int, nombre: str, correo: str, es_miembro: bool):
        self.codigo = codigo               # Código único de cliente
        self.nombre = nombre               # Nombre completo
        self.correo = correo               # Correo de contacto
        self.es_miembro = es_miembro       # Indica si pertenece al programa de fidelidad

    def __str__(self) -> str:
        estado = "Miembro activo" if self.es_miembro else "Cliente ocasional"
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Correo: {self.correo} | Estado: {estado}"
