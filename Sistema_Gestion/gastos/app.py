from flask import Flask, jsonify, request, render_template

from datos import crear_estado
from main import (
    inicializar_sistema,
    preparar_gasto,
    confirmar_gasto,
    obtener_datos_pagina
)
from gastos import deshacer_ultimo

app = Flask(__name__)

estado = crear_estado()
inicializar_sistema(estado)


@app.route("/")
def index():
    datos = obtener_datos_pagina(estado)

    return render_template("index.html", **datos)


@app.route("/api/estado", methods=["GET"])
def api_estado():
    return jsonify({
        "exito": True,
        "mensaje": "Datos cargados correctamente.",
        "datos": obtener_datos_pagina(estado)
    })


@app.route("/api/agregar", methods=["POST"])
def api_agregar():
    datos = request.get_json(silent=True) or {}

    gasto, error = preparar_gasto(estado, datos)

    if error:
        return jsonify({
            "exito": False,
            "mensaje": error,
            "datos": obtener_datos_pagina(estado)
        })

    return jsonify({
        "exito": True,
        "mensaje": "Gasto agregado a pendientes.",
        "datos": obtener_datos_pagina(estado)
    })


@app.route("/api/categorizar", methods=["POST"])
def api_categorizar():
    datos = request.get_json(silent=True) or {}

    try:
        categoria_id = int(datos.get("categoria_id"))
    except (TypeError, ValueError):
        return jsonify({
            "exito": False,
            "mensaje": "Seleccione una categoría válida.",
            "datos": obtener_datos_pagina(estado)
        })

    gasto, error = confirmar_gasto(estado, categoria_id)

    if error:
        return jsonify({
            "exito": False,
            "mensaje": error,
            "datos": obtener_datos_pagina(estado)
        })

    return jsonify({
        "exito": True,
        "mensaje": "Gasto confirmado y guardado.",
        "datos": obtener_datos_pagina(estado)
    })


@app.route("/api/deshacer", methods=["POST"])
def api_deshacer():
    gasto = deshacer_ultimo(estado)

    if gasto is None:
        return jsonify({
            "exito": False,
            "mensaje": "No hay gastos para deshacer.",
            "datos": obtener_datos_pagina(estado)
        })

    return jsonify({
        "exito": True,
        "mensaje": "Último gasto deshecho.",
        "datos": obtener_datos_pagina(estado)
    })


if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)