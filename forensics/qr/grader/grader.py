#!/bin/python

def grade(arg, key):
    if "InnoCTF{was ist das}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
