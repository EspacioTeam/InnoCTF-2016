#!/bin/python

def grade(arg, key):
    if "InnoCTF{Chris Tavares}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
