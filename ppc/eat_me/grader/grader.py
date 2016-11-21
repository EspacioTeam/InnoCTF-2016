#!/bin/python

def grade(arg, key):
    if "InnoCTF{Gr347_5ucc355!_y0u_4r3_w1n!_u53_7h1s_fl4g}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
