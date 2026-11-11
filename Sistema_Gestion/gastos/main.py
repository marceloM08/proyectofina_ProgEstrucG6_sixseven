from datetime import datetime

from datos import CATEGORIAS_INICIALES
from almacenamiento import (
    cargar_gastos,
    guardar_gastos,
    cargar_categorias,
    guardar_categorias
)
from gastos import capturar_datos, categorizar_siguientes, deshacer_ultimo
from arbol import buscar_categoria, mostrar_arbol, total_arbol
from grafo import construir_grafo


def validar_monto(valor):
    try:
        monto = float(valor)
    except (TypeError, ValueError):
        return None, "El monto debe ser un número válido."

    if monto <= 0:
        return None, "El monto debe ser mayor que 0."

    return monto, None


def validar_texto(valor, nombre_campo):
    if valor is None:
        return None, f"El campo {nombre_campo} es obligatorio."

    valor = valor.strip()

    if not valor:
        return None, f"El campo {nombre_campo} es obligatorio."

    return valor, None


def validar_fecha(valor):
    fecha, error = validar_texto(valor, "fecha")

    if error:
        return None, error

    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        return None, "La fecha debe tener el formato AAAA-MM-DD."

    return fecha, None


def convertir_personas(valor):
    if not valor:
        return []

    personas = valor.split(",")

    return [persona.strip() for persona in personas if persona.strip()]


def preparar_gasto(estado, datos_formulario):
    monto, error = validar_monto(datos_formulario.get("monto"))

    if error:
        return None, error

    descripcion, error = validar_texto(
        datos_formulario.get("descripcion"),
        "descripción"
    )

    if error:
        return None, error

    fecha, error = validar_fecha(datos_formulario.get("fecha"))

    if error:
        return None, error

    metodo_pago, error = validar_texto(
        datos_formulario.get("metodo_pago"),
        "método de pago"
    )

    if error:
        return None, error

    lugar = datos_formulario.get("lugar", "").strip()
    personas = convertir_personas(datos_formulario.get("personas", ""))

    gasto, error = capturar_datos(
    estado,
    monto,
    descripcion,
    fecha,
    metodo_pago,
    lugar,
    personas
)

    if error:
        return None, error

    return gasto, None


def confirmar_gasto(estado, categoria_id):
    categoria = buscar_categoria(estado["categorias"], categoria_id)

    if categoria is None:
        return None, "La categoría seleccionada no existe."

    gasto, error = categorizar_siguientes(estado, categoria_id)

    if error:
        return None, error

    return gasto, None


def obtener_datos_pagina(estado):
    gastos = cargar_gastos()
    categorias = estado["categorias"]
    grafo = construir_grafo(gastos, categorias)

    for gasto in gastos:
        gasto["categoria"] = "Sin categoría"

        categoria = buscar_categoria(
            categorias,
            gasto.get("categoria_id")
        )

        if categoria:
            gasto["categoria"] = categoria["nombre"]

        gasto.setdefault("personas", [])
        gasto.setdefault("lugar", "")
        gasto.setdefault("metodo_pago", "Efectivo")

    return {
        "gastos": gastos,
        "categorias": categorias,
        "arbol": mostrar_arbol(categorias),
        "aristas": grafo.get("aristas", []),
        "total_general": total_arbol(categorias, gastos, None)
    }

def inicializar_sistema(estado):
    categorias = cargar_categorias()

    if not categorias:
        categorias = CATEGORIAS_INICIALES
        guardar_categorias(categorias)

    estado["categorias"] = categorias