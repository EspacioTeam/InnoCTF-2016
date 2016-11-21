#!/bin/python

def grade(arg, key):
    if "InnoCTF{London}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
