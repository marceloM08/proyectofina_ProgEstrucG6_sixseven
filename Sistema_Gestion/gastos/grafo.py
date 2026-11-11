from arbol import buscar_categoria 
def crear_grafo():
    return {
        "nodos": {},
        "aristas": []
    }


def agregar_nodo(grafo, tipo, nombre):
    clave = tipo + ":" + nombre

    if clave not in grafo["nodos"]:
        grafo["nodos"][clave] = {
            "tipo": tipo,
            "nombre": nombre
        }

    return clave


def agregar_arista(grafo, origen, destino, tipo_relacion):
    arista = {
        "origen": origen,
        "destino": destino,
        "tipo": tipo_relacion
    }

    if arista not in grafo["aristas"]:
        grafo["aristas"].append(arista)


def construir_grafo(gastos, categorias):
    grafo = crear_grafo()

    for gasto in gastos:
        gasto_id = "gasto:" + str(gasto["id"])
        agregar_nodo(grafo, "gasto", str(gasto["id"]))

        categoria = buscar_categoria(categorias, gasto["categoria_id"])

        if categoria:
            categoria_id = agregar_nodo(grafo, "categoria", categoria["nombre"])
            agregar_arista(grafo, gasto_id, categoria_id, "pertenece_a")

        metodo = agregar_nodo(grafo, "metodo_pago", gasto["metodo_pago"])
        agregar_arista(grafo, gasto_id, metodo, "pagado_con")

        if gasto["lugar"]:
            lugar = agregar_nodo(grafo, "lugar", gasto["lugar"])
            agregar_arista(grafo, gasto_id, lugar, "realizado_en")

        for persona in gasto["personas"]:
            persona_id = agregar_nodo(grafo, "persona", persona)
            agregar_arista(grafo, gasto_id, persona_id, "compartido_con")

    return grafo


def gastos_por_lugar(gastos):
    lugares = {}

    for gasto in gastos:
        lugar = gasto["lugar"]

        if lugar:
            lugares[lugar] = lugares.get(lugar, 0) + gasto["monto"]

    return lugares


def gastos_por_persona(gastos):
    personas = {}

    for gasto in gastos:
        for persona in gasto["personas"]:
            personas[persona] = personas.get(persona, 0) + gasto["monto"]

    return personas