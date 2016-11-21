#!/bin/python

def grade(arg, key):
    if "InnoCTF{@dm1n1str@t0r}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
