from cola import crear_cola
from pila import crear_pila
from lista_doble import crear_lista

CATEGORIAS_INICIALES = [
    {"id": 1, "nombre": "Comida", "padre_id": None},
    {"id": 2, "nombre": "Transporte", "padre_id": None},
    {"id": 3, "nombre": "Servicios", "padre_id": None},
    {"id": 4, "nombre": "Ocio", "padre_id": None},
    {"id": 5, "nombre": "Salud", "padre_id": None},
    {"id": 6, "nombre": "Otros", "padre_id": None}
]


def crear_gasto(monto, descripcion, fecha, categoria_id=None,
                metodo_pago="Efectivo", lugar="", personas=None):
    return {
        "id": 0,
        "monto": float(monto),
        "descripcion": descripcion,
        "fecha": fecha,
        "categoria_id": categoria_id,
        "metodo_pago": metodo_pago,
        "lugar": lugar,
        "personas": personas if personas else []
    }


def crear_estado():
    return {
        "pendientes": crear_cola(),
        "recientes": crear_pila(),
        "gastos": crear_lista(),
        "categorias": [],
        "siguiente_id_gasto": 1,
        "siguiente_id_categoria": 7
    } 