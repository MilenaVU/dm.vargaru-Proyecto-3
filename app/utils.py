#definir clases para usar con productos
def calcular_calorias(ingredientes):
    return round(sum([ing.calorias for ing in ingredientes]) * 0.95, 2)

def calcular_costo(ingredientes):
    return sum([ing.precio for ing in ingredientes])

def calcular_rentabilidad(precio_producto, ingredientes):
    costo = calcular_costo(ingredientes)
    return precio_producto - costo

def encontrar_producto_mas_rentable(productos):
    return max(productos, key=lambda producto: producto.calcular_rentabilidad()).nombre
