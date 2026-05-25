
# -------------------------------------------------------
# Nombre del estudiante: Tatiana Isabel Hoyos Vertel
# Grupo: 256
# Programa: Ingeniería de Sistemas
# Código Fuente: Autoría propia
# Descripción: Programa que gestiona los precios de un menú de
# restaurante y aplica un descuento del 15% a los
# productos que cumplan ciertas condiciones.
# -------------------------------------------------------

# Matriz de productos
# [Nombre, Categoría, Precio Base]

menu = [
    ["Hamburguesa", "Comida Rapida", 25000],
    ["Pizza", "Comida Rapida", 32000],
    ["Helado", "Postres", 12000],
    ["Fresas con crema", "Postres", 18000],
    ["Gaseosa", "Bebidas", 5000],
    ["Malteada", "Bebidas", 15000]
]

# Parámetros globales
categoria_objetivo = "Postres"
umbral_precio = 15000

# Función para calcular el precio final
def calcular_precio_final(categoria, precio_base):

    # Validar condiciones para aplicar descuento
    if categoria == categoria_objetivo and precio_base > umbral_precio:
        
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento

    else:
        precio_final = precio_base

    return precio_final


# Mostrar resultados
print("========================================")
print("   MENÚ DEL RESTAURANTE - PROMOCIONES")
print("========================================\n")

# Recorrer matriz
for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Llamar función
    precio_final = calcular_precio_final(categoria, precio_base)

    # Mostrar información
    print(f"Producto: {nombre}")
    print(f"Categoría: {categoria}")
    print(f"Precio Base: ${precio_base:,.0f}")
    print(f"Precio Final: ${precio_final:,.0f}")
    print("----------------------------------------")