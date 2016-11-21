#!/bin/python

def grade(arg, key):
    if "InnoCTF{3xp@nd_th3_br0ws3r}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
