#!/bin/python

def grade(arg, key):
    if "InnoCTF{xorcipherisnotsecure}" in key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
