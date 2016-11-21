#!/bin/python

def grade(arg, key):
    if "InnoCTF{ppbmgjmk}" in key or "InnoCTF{ppbmgjkk}" in key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
