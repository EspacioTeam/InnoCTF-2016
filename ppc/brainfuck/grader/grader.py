#!/bin/python

def grade(arg, key):
    if "InnoCTF{e51689c8}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
