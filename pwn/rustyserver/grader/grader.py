#!/bin/python

def grade(arg, key):
    if "InnoCTF{D4mn!_H0w_d1d_y0u_f1nd_m3?}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
