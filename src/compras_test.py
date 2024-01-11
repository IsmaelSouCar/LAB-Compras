from compras import *

def test_lee_compras():
    compras = lee_compras("data\compras.csv")
    print("EJERCICIO 1\n")
    print(f"Número de registros leídos: {len(compras)}\n")
    print(f"Tres primeros registros: {compras[:3]}\n")
    print(f"Tres últimos registros: {compras[-3:]}\n")

def test_compra_maxima_minima_provincia(reg):
    print("EJERCICIO 2\n")
    compras_provincia = compra_maxima_minima_provincia(reg, "Huelva")
    print(f"Importe máximo de Huelva: {compras_provincia[0]} . Importe mínimo: {compras_provincia[1]}\n")
    compras_none = compra_maxima_minima_provincia(reg)
    print(f"Importe máximo de None: {compras_none[0]} . Importe mínimo: {compras_none[1]}\n")

def test_hora_menor_afluencia(reg):
    print("EJERCICIO 3\n")
    hora = hora_menor_afluencia(reg)
    print(f"La hora con menor afluencia es: {hora[0]}h. con {hora[1]} llegadas.\n")

def test_supermercados_mas_facturacion(reg):
    print("EJERCICIO 4\n")
    ranking = supermercados_mas_facturacion(reg, 2)
    print(ranking)

if __name__=='__main__':
    reg = lee_compras("data\compras.csv")
    test_lee_compras()
    test_compra_maxima_minima_provincia(reg)
    test_hora_menor_afluencia(reg)
    test_supermercados_mas_facturacion(reg)