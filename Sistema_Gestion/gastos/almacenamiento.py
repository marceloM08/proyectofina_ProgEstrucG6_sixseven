#Este archivo se encarga exclusivamente de leer y escribir JSON
import json
import os

ARCHIVO_GASTOS = "gastos.json"
ARCHIVO_CATEGORIAS = "categorias.json"


def cargar_gastos():
    if not os.path.exists(ARCHIVO_GASTOS):
        return []

    with open(ARCHIVO_GASTOS, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []


def guardar_gastos(gastos):
    with open(ARCHIVO_GASTOS, "w", encoding="utf-8") as archivo:
        json.dump(gastos, archivo, indent=4, ensure_ascii=False)


def cargar_categorias():
    if not os.path.exists(ARCHIVO_CATEGORIAS):
        return []

    with open(ARCHIVO_CATEGORIAS, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []


def guardar_categorias(categorias):
    with open(ARCHIVO_CATEGORIAS, "w", encoding="utf-8") as archivo:
        json.dump(categorias, archivo, indent=4, ensure_ascii=False)