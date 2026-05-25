
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
