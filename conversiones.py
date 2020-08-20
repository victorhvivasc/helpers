# import numpy as np
# import mecanica_fisica
# from herramientas import validate

# Bases: 1 km = 1000 m = 100000 cm = 1000000 mm
# 1 milla = 1760 yardas = 5280 pies = 63360 pulgadas


def longitud(valor, u_e, u_s):
    """conversion de unidades de representacion entre sistema de unidades o escalas
    valor: int o float suministrado
    u_e: unidades originales del valor suministrado posibles valores km, m, cm, mm, milla, yarda, pie, pulgada
    e_s: unidades de salida, al cual se desea llegar posibles valores km, m, cm, mm, milla, yarda, pie, pulgada
    """
    if u_e == u_s:
        return valor
    elif u_e == 'km':
        if u_s == 'm':
            return valor*1000
        elif u_s == 'cm':
            return valor*1000*100
        elif u_s == 'mm':
            return valor*1000*100*10
        elif u_s == 'milla':
            return valor*0.621371
        elif u_s == 'yarda':
            return valor*1093.61
        elif u_s == 'pie':
            return valor*3280.84
        elif u_s == 'pulgada':
            return valor*39370.1
    elif u_e == 'm':
        if u_s == 'km':
            return valor/1000
        elif u_s == 'cm':
            return valor*100
        elif u_s == 'mm':
            return valor*100*10
        elif u_s == 'milla':
            return valor/1609.34
        elif u_s == 'yarda':
            return valor*1.0936133
        elif u_s == 'pie':
            return valor*3.28084
    elif u_e == 'cm':
        if u_s == 'km':
            return valor/100*1000
        elif u_s == 'm':
            return valor/100
        elif u_s == 'mm':
            return valor*10
        elif u_s == 'milla':
            return valor/160934
        elif u_s == 'yarda':
            return valor/91.44
        elif u_s == 'pie':
            return valor/30.48
        elif u_s == 'pulgada':
            return valor/2.54
    elif u_e == 'mm':
        if u_s == 'km':
            return valor/(1000*100*10)
        elif u_s == 'm':
            return valor/1000
        elif u_s == 'cm':
            return valor/10
        elif u_s == 'milla':
            return valor/1609340
        elif u_s == 'yarda':
            return valor/914.4
        elif u_s == 'pie':
            return valor/304.8
        elif u_s == 'pulgada':
            return valor/25.4


numero_de_llamada = 539637747
