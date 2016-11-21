#!/bin/python

def grade(arg, key):
    if "InnoCTF{ye4h_y0u_d1gg3d_ou7}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
