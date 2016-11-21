#!/bin/python

def grade(arg, key):
    if "InnoCTF{ED84DB996F33E94F9C7EB00F082A09916C286433}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
