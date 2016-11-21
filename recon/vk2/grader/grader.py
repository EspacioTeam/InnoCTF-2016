#!/bin/python

def grade(arg, key):
    if "InnoCTF{Р07-19НЯ}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
