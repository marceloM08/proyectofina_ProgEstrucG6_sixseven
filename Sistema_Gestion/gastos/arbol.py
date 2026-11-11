def obtener_hijos(categorias, id_padre):
    hijos = []

    for categoria in categorias:
        if categoria["padre_id"] == id_padre:
            hijos.append(categoria)

    return hijos


def mostrar_arbol(categorias, id_padre=None, nivel=0, lineas=None):
    if lineas is None:
        lineas = []

    hijos = obtener_hijos(categorias, id_padre)

    for categoria in hijos:
        lineas.append("  " * nivel + "- " + categoria["nombre"])
        mostrar_arbol(
            categorias,
            categoria["id"],
            nivel + 1,
            lineas
        )

    return "\n".join(lineas)


def buscar_categoria(categorias, id_categoria):
    for categoria in categorias:
        if categoria["id"] == id_categoria:
            return categoria

    return None


def total_arbol(categorias, gastos, id_categoria=None):
    total = 0.0

    for gasto in gastos:
        if gasto.get("categoria_id") == id_categoria:
            total += float(gasto.get("monto", 0))

    for hijo in obtener_hijos(categorias, id_categoria):
        total += total_arbol(categorias, gastos, hijo["id"])

    return total