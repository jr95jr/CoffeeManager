IVA_RATE = 0.13  # 13%

def calcular_factura(subtotal: float):
    if subtotal < 0:
        raise ValueError("Subtotal no puede ser negativo")
    iva = round(subtotal * IVA_RATE, 2)
    total = round(subtotal + iva, 2)
    return round(subtotal, 2), iva, total
