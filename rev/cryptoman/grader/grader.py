#!/bin/python

def grade(arg, key):
    if "InnoCTF{crypt0_m4g1c14n}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
