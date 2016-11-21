#!/bin/python

def grade(arg, key):
    if "InnoCTF{thanksforthephoto!}" in key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
