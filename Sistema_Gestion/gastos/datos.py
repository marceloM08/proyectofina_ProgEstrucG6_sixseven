#Se llaman las funciones desde la carpeta de estructuras. 
from cola import crear_cola
from pila import crear_pila
from lista_doble import crear_lista
#se marcan las categorias de gastos que se pueden agregar al sistema.
categories = ["Comida", "Transporte", "Servicios", "Ocio", "Salud", "Otros"]

contador = {"id": 0} #El contador se utiliza para asignar un ID único a cada gasto creado. Se inicializa en 0 y se incrementa cada vez que se crea un nuevo gasto.


def crear_gasto(monto, descripcion, fecha, categorias = None):
    contador["id"] += 1
    return {
        "id": contador["id"],
        "monto": monto,
        "descripcion": descripcion,
        "fecha": fecha,
        "categoria": categorias,
}

def crear_estado():
    return {
        "pendientes": crear_cola(),
        "recientes": crear_pila(),
        "gastos": crear_lista(),
    }
