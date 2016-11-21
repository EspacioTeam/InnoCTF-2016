#!/bin/python

def grade(arg, key):
    if "InnoCTF{l3ts_pl4y_th3_g4m3}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
