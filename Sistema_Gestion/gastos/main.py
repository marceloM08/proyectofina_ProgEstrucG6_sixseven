from datos import crear_estado, categories
from gastos import (capturar_datos, categorizar_siguientes, deshacer_ultimo, listar_gastos, total_general, total_por_categoria)
from cola import ver_frente

def pedir_monto():
    while True:
        try: 
            monto = float(input("Monto: "))
            if monto > 0:
                return monto
            print("El monto debe ser mayor que 0.")
        except ValueError:
            print("Error: Ingrese un numero valido porfavor.")

def pedir_categoria():
    