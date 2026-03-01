from flask import Flask, render_template, request, redirect
from database import crear_tabla, Inventario

app = Flask(__name__)

# Crear tabla al iniciar
crear_tabla()

# Crear objeto inventario
inventario = Inventario()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/productos")
def productos():
    productos = inventario.obtener_todos()
    return render_template("productos.html", productos=productos)


@app.route("/clientes")
def clientes():
    return render_template("clientes.html")


@app.route("/factura")
def factura():
    return render_template("factura.html")


@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    cantidad = int(request.form["cantidad"])
    precio = float(request.form["precio"])

    inventario.agregar_producto(nombre, cantidad, precio)
    return redirect("/productos")


@app.route("/eliminar/<int:id>")
def eliminar(id):
    inventario.eliminar_producto(id)
    return redirect("/productos")


if __name__ == "__main__":
    app.run(debug=True)