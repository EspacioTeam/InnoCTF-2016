#!/bin/python

def grade(arg, key):
    if "InnoCTF{Win32.Trojaner.DeutschePorno}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
