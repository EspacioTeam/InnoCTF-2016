#!/bin/python

def grade(arg, key):
    if "InnoCTF{sngwwlsik}" in key or "InnoCTF{sngwwlsic}" in key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
