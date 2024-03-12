def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicando el porcentaje al monto total de la compra.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar.
            Por defecto es 10.

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Llamadas a la función calcular_descuento
monto_compra1 = 150
porcentaje_descuento1 = 15

monto_compra2 = 200

descuento1 = calcular_descuento(monto_compra1, porcentaje_descuento1)
descuento2 = calcular_descuento(monto_compra2)

monto_final1 = monto_compra1 - descuento1
monto_final2 = monto_compra2 - descuento2

# Resultados
print("Resultados de la primera llamada:")
print(f"Monto de la compra: {monto_compra1}")
print(f"Porcentaje de descuento: {porcentaje_descuento1}%")
print(f"Descuento aplicado: {descuento1}")
print(f"Monto final a pagar: {monto_final1}")

print("\nResultados de la segunda llamada:")
print(f"Monto de la compra: {monto_compra2}")
print(f"Porcentaje de descuento (por defecto): 10%")
print(f"Descuento aplicado: {descuento2}")
print(f"Monto final a pagar: {monto_final2}")
