#!/bin/python

def grade(arg, key):
    if "InnoCTF{Neil Flynn}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
