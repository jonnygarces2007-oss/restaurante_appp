# restaurante_appp

# 📋 Sistema Básico de Gestión de Restaurante

**Asignatura:** Programación Orientada a Objetos  
**Semana:** 5  
**Objetivo académico:** Aplicar correctamente los conceptos de identificadores, convenciones de nombres, tipos de datos básicos, clases, objetos, métodos, modularidad y buenas prácticas de programación en Python.

---

##  Propósito del proyecto
Este sistema permite gestionar de forma sencilla los elementos principales de un restaurante: los productos disponibles (platos y bebidas) y los clientes registrados. No se trata de una aplicación compleja con interfaz gráfica ni menús interactivos, sino de un ejemplo práctico que demuestra cómo estructurar un programa usando Programación Orientada a Objetos y organización modular.

---

##  Conceptos aplicados
Durante el desarrollo se pusieron en práctica los siguientes temas:
- Definición de clases y creación de objetos.
- Uso del constructor `__init__` para inicializar atributos.
- Aplicación de tipos de datos básicos: `str`, `int`, `float`, `bool`.
- Uso de listas como estructura de datos compuesta para almacenar conjuntos de objetos.
- Métodos para agregar, consultar y mostrar información.
- Método especial `__str__()` para representar objetos como texto legible.
- Convenciones de nombres en Python:
  - `PascalCase` para nombres de clases.
  - `snake_case` para archivos, variables, atributos y métodos.
- Organización del código en módulos independientes.
- Importación correcta entre archivos del proyecto.
- Anotaciones de tipo para mayor claridad y mantenibilidad.

---

## 📁 Estructura detallada del proyecto

restaurante_app/│├── modelos/ # Contiene las clases que representan las entidades del sistema│ ├── init.py # Indica que la carpeta es un paquete de Python│ ├── producto.py # Clase que define las características de un producto│ └── cliente.py # Clase que define los datos de un cliente│├── servicios/ # Contiene la lógica de gestión y almacenamiento de información│ ├── init.py # Indica que la carpeta es un paquete de Python│ └── restaurante.py # Clase principal que administra listas de productos y clientes│├── main.py # Archivo principal: punto de inicio, creación de objetos y ejecución└── README.md # Documentación general del proyecto



---

## 🧩 Descripción de las clases

### 1. Clase `Producto`
**Ubicación:** `modelos/producto.py`  
Representa cualquier elemento que se pueda vender en el restaurante, ya sea un plato de comida o una bebida.

**Atributos:**
- `identificador: int` → Número único que identifica al producto.
- `nombre: str` → Nombre descriptivo del plato o bebida.
- `precio: float` → Valor de venta en dólares.
- `es_bebida: bool` → Indica si el producto es bebida (`True`) o comida (`False`).
- `disponibilidad: int` → Cantidad de unidades disponibles en inventario.

**Métodos:**
- `__init__()` → Constructor que asigna valores iniciales.
- `__str__()` → Devuelve una cadena con toda la información del producto.

---

### 2. Clase `Cliente`
**Ubicación:** `modelos/cliente.py`  
Representa a una persona que acude al restaurante y puede estar registrada en el sistema.

**Atributos:**
- `codigo: int` → Número único de identificación del cliente.
- `nombre: str` → Nombre completo del cliente.
- `correo: str` → Dirección de correo electrónico para contacto.
- `es_miembro: bool` → Indica si pertenece al programa de fidelidad (`True`) o es cliente ocasional (`False`).

**Métodos:**
- `__init__()` → Constructor para inicializar los datos.
- `__str__()` → Muestra la información del cliente en formato texto.

---

### 3. Clase `Restaurante`
**Ubicación:** `servicios/restaurante.py`  
Es la clase encargada de gestionar la información, actuar como contenedor y proveer métodos para administrar los datos.

**Atributos:**
- `nombre: str` → Nombre comercial del restaurante.
- `lista_productos: list[Producto]` → Lista donde se guardan todos los productos registrados.
- `lista_clientes: list[Cliente]` → Lista donde se almacenan los clientes registrados.

**Métodos:**
- `__init__()` → Inicializa el nombre y crea listas vacías.
- `agregar_producto()` → Recibe un objeto `Producto` y lo añade a la lista.
- `agregar_cliente()` → Recibe un objeto `Cliente` y lo añade a la lista.
- `mostrar_productos()` → Recorre la lista y muestra cada producto en consola.
- `mostrar_clientes()` → Recorre la lista y muestra cada cliente en consola.

---

## ▶️ ¿Cómo ejecutar el programa?
Sigue estos pasos para ver el funcionamiento:

1. **Requisito previo:** Tener instalado Python 3.8 o una versión superior.
2. **Descargar o clonar el proyecto:**
   ```bash
   git clone <enlace-del-repositorio>
   cd restaurante_app

   ## Ejemplo de salida en consola##
   === Sistema de Gestión: Sabor Andino ===

--- Menú de Productos ---
ID: 1 | Nombre: Encebollado | Tipo: Comida | Precio: $5.75 | Disponibles: 20
ID: 2 | Nombre: Jugo de naranja | Tipo: Bebida | Precio: $2.50 | Disponibles: 30

--- Lista de Clientes ---
Código: 101 | Nombre: María López | Correo: maria@correo.com | Estado: Miembro activo
Código: 102 | Nombre: Juan Pérez | Correo: juan@correo.com | Estado: Cliente ocasional





El proyecto está organizado de forma modular, lo que significa que si en el futuro queremos agregar nuevas funciones o incluso crear clases adicionales, podremos hacerlo sin tener que cambiar la estructura principal que ya funciona. Se puso mucho cuidado en usar nombres claros y una lógica sencilla, para que sea fácil de leer, entender y aprender los conceptos básicos de la Programación Orientada a Objetos.
