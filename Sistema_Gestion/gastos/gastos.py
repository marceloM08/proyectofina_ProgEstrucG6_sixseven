from cola import encolar, desencolar
from pila import apilar, desapilar
from datos import crear_gasto
from lista_doble import insertar_final, eliminar, a_lista

def capturar_datos(estado, monto, descripcion, fecha): #El capturar_datos crea un gasto con los datos proporcionados y lo encola en la lista de pendientes del estado.
    gasto = crear_gasto(monto, descripcion, fecha)
    encolar(estado["pendientes"], gasto)
    return gasto

def categorizar_siguientes(estado, categoria):
    gasto = desencolar(estado["pendientes"])
    if gasto is None:
        return None
    gasto["categoria"] = categoria
    nodo = insertar_final(estado["gastos"], gasto)
    apilar(estado["recientes"], nodo)
    return gasto

def deshacer_ultimo(estado):
    nodo = desapilar(estado["recientes"])
    if nodo is None:
        return None
    eliminar(estado["gastos"], nodo)
    return nodo["dato"]

def listar_gastos(estado):
    return a_lista(estado["gastos"])

def total_general(estado):
    return sum(g["monto"] for g in listar_gastos(estado))

def total_por_categoria(estado):
    totales = {}
    for g in listar_gastos(estado):
        cat = g["categoria"]
        totales[cat] = totales.get(cat, 0) + g["monto"]
    return totales