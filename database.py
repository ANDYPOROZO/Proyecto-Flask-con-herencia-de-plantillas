import sqlite3

def conectar():
    conn = sqlite3.connect("inventario.db")
    conn.row_factory = sqlite3.Row
    return conn

def crear_tabla():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()


class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = {}

    def cargar_desde_db(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        filas = cursor.fetchall()

        for fila in filas:
            producto = Producto(fila["id"], fila["nombre"], fila["cantidad"], fila["precio"])
            self.productos[producto.id] = producto

        conn.close()

    def agregar_producto(self, nombre, cantidad, precio):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
            (nombre, cantidad, precio)
        )
        conn.commit()
        conn.close()

    def eliminar_producto(self, id):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
        conn.commit()
        conn.close()

    def obtener_todos(self):
        self.cargar_desde_db()
        return self.productos.values()