from almacenamiento import cargar_gastos, guardar_gastos
from datos import crear_gasto
from cola import encolar, desencolar
from pila import apilar, desapilar
from lista_doble import insertar_final, eliminar, a_lista


def capturar_datos(estado, monto, descripcion, fecha,
                   metodo_pago="Efectivo", lugar="", personas=None):
    gasto = crear_gasto(
        monto,
        descripcion,
        fecha,
        metodo_pago=metodo_pago,
        lugar=lugar,
        personas=personas
    )

    gasto["id"] = estado["siguiente_id_gasto"]
    estado["siguiente_id_gasto"] += 1

    encolar(estado["pendientes"], gasto)

    return gasto, None


def categorizar_siguientes(estado, categoria_id):
    gasto = desencolar(estado["pendientes"])

    if gasto is None:
        return None, "No hay gastos pendientes."

    gasto["categoria_id"] = categoria_id

    nodo = insertar_final(estado["gastos"], gasto)
    apilar(estado["recientes"], nodo)

    gastos_guardados = cargar_gastos()

    if not isinstance(gastos_guardados, list):
        gastos_guardados = []

    gastos_guardados.append(gasto)
    guardar_gastos(gastos_guardados)

    return gasto, None

def deshacer_ultimo(estado):
    nodo = desapilar(estado["recientes"])

    if nodo is None:
        return None

    eliminar(estado["gastos"], nodo)

    gastos_guardados = cargar_gastos()

    if not isinstance(gastos_guardados, list):
        gastos_guardados = []

    id_gasto = nodo["dato"]["id"]

    gastos_guardados = [
        gasto for gasto in gastos_guardados
        if gasto.get("id") != id_gasto
    ]

    guardar_gastos(gastos_guardados)

    return nodo["dato"]