
"""
dicc_productos = {}

contador = 0

while contador < 3:
    nombre_producto = input("Ingrese el nombre del producto")
    precio = input("Ingresa el precio")
    dicc_productos.update({nombre_producto:precio})
    contador = contador + 1

"""



"""
def descuento(precio:int, porcentaje_desc:int):
    descuento = precio * porcentaje_desc/100
    precio_final = precio - descuento
    return precio_final



precio = int(input("Ingrese el precio del producto"))
porcentaje_desc = int(input("Ingrese el porcentaje de descuento"))


precio_calculado = descuento(precio, porcentaje_desc)
print(precio_calculado)
"""


ventas_diarias = {"Lunes":20000,
                  "Martes":15000,
                  "Miercoles":23000,
                  "Jueves":60000,
                  "Viernes":18000,
                  "Sabado":33000,
                  "Domingo":40000,
            }


def promedio_ventas( lista_ventas ):
    acu = 0
    for key , ventas in lista_ventas.items():        
        acu = ventas + acu
    promedio = acu / 7
    return promedio



promedio_calculado = promedio_ventas(ventas_diarias)
print(promedio_calculado)