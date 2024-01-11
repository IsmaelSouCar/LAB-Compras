from collections import *
import csv
from datetime import datetime
from typing import NamedTuple


Compra = NamedTuple('Compra',
                    [('dni', str),
                     ('supermercado', str),
                     ('provincia', str),
                     ('fecha_llegada', datetime),
                     ('fecha_salida', datetime),
                     ('total_compra', float)]
                    )

def lee_compras(ruta):
    res = []
    with open(ruta, encoding= "utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra in lector:
            fecha_llegada = datetime.strptime(fecha_llegada, "%d/%m/%Y %H:%M")
            fecha_salida = datetime.strptime(fecha_salida, "%d/%m/%Y %H:%M")
            total_compra = float(total_compra)
            res.append(Compra(dni, supermercado, provincia, fecha_llegada, fecha_salida, total_compra))
    return res
    
def compra_maxima_minima_provincia(reg, provincia=None):
    compras_provincia=[]
    for compra in reg:
        if compra.provincia==provincia or provincia==None:
            compras_provincia.append(compra.total_compra)
    maximo = max(compras_provincia)
    minimo = min(compras_provincia)
    res = [maximo, minimo]
    return res

def hora_menor_afluencia(reg):
    res = []
    clientes_por_hora = dict()
    for compra in reg:
        hora_llegada = compra.fecha_llegada.hour 
        clientes_por_hora[hora_llegada] = clientes_por_hora.get(hora_llegada, 0) + 1
    hora_menos_clientes = min(clientes_por_hora, key= clientes_por_hora.get)
    num_clientes_menor = clientes_por_hora[hora_menos_clientes]
    res = [hora_menos_clientes, num_clientes_menor]
    return res

def supermercados_mas_facturacion(reg, n=3):
    facturacion_por_supermercado = dict()
    for compra in reg:
        facturacion_por_supermercado[compra.supermercado] = facturacion_por_supermercado.get(compra.supermercado, 0) + compra.total_compra
    ranking =sorted(facturacion_por_supermercado, key = facturacion_por_supermercado.get, reverse= True)[:n]
    ranking_importe = enumerate(["hola","adios"])
    print(ranking)
    print(ranking_importe)
    return ranking_importe

supermercados_mas_facturacion(lee_compras("data\compras.csv"), 2)