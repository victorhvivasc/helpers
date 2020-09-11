# -*- coding: utf-8 -*-
# diccionario de unidades equivalentes para ser usadas por funcion de simplificacion
import itertools

conversiones1 = {
    '(m3/s).(m3/s)': 'm⁶/s²',
    '(s).(s)': 's²',
    '(s2).(s)': "s³",
    '(s).(s2)': "s³",
    '(s²).(s)': "s³",
    '(s).(s²)': "s³",
}
u1 = '(m).(m)'
u2 = 'm²'
unidades = ['m', 'k', 's', 'm', 'm2', 'm3', 'm4', 'm5', 'm6', 's', 's2', 's3', 's4', 's5', 's6',
            'k', 'k2', 'k3', 'k4', 'k5', 'k6']
opciones = {}
for x in itertools.permutations(unidades, 2):
    if (x[0] != 'kg') and (x[1] != 'kg'):
        if x[0] == x[1]:
            opciones[f"({x[0]}).({x[1]})"] = f"{x[0]}²"
        else:
            if (len(x[0]) < 2) and (len(x[1]) < 2):
                opciones[f"({x[0]}).({x[1]})"] = f"{x[0]}.{x[1]}"
            else:
                if x[0][0] == x[1][0]:
                    if len(x[0]) < 2:
                        exp0 = 1
                    else:
                        exp0 = int(x[0][-1])
                    if len(x[1]) < 2:
                        exp1 = 1
                    else:
                        exp1 = int(x[1][-1])
                    exp = exp0 + exp1
                    opciones[f"({x[0]}).({x[1]})"] = f"{x[0][0]}{exp}"

con_m = opciones
