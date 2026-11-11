def crear_cola(): #Se crea la cola, vacia
    return []

def encolar(cola, dato):
    cola.append(dato)

def desencolar(cola):
    return cola.pop(0) if cola else None #se valida que no este vacia, si lo esta retorna none. si no, retorna el primer elemento de la cola y lo elimina de la misma

def esta_vacia(cola):
    return len(cola) == 0 #validacion en caso de que este vacia.

def ver_frente(cola):
    return cola[0] if cola else None #Si esta vacia retorna none, si no, retorna el primer elemento de la cola sin eliminarlo.