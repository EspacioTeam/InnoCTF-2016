#!/bin/python

def grade(arg, key):
    if "InnoCTF{banana}" == key or "InnoCTF{flagisbanana}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
