def promedio_precios1(precios):
    """ Calcula el promedio de los precios convertibles a float.

    Omite los valores no convertibles.
    Devuelve None si no hay precios validos.
    Redondea el promedio a dos decimales.
    """
    precios_validos = []

    for precio in precios:
        try:
            numero = float(precio)
            precios_validos.append(numero)
        except (ValueError, TypeError):
            continue

    if len(precios_validos) == 0:
        return None

    promedio = sum(precios_validos) / len(precios_validos)
    return round(promedio, 2)


