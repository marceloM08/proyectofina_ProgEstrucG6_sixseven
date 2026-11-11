def crear_pila(): #Se crea la pila vacia
    return []

def apilar(pila, dato): #Se apila un dato en la pila, se agrega al final de la lista.
    pila.append(dato)

def desapilar(pila): #Siguiendo el principio LIFO, se desapila el ultimo elemento agregado a la pila.
    return pila.pop() if pila else None

def ver_tope(pila): #Se revisa el tope de la pila, osea el ultimo elemento agregado SIN eliminarlo.
    return pila[-1] if pila else None

def esta_vacia(pila): #validacion en caso que este vacia, por motivos de eficiencia para no pegar esto en cada funcion del programa.
    return len(pila) == 0 