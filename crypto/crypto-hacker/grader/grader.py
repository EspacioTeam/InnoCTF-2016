#!/bin/python

def grade(arg, key):
    if "InnoCTF{f@cT0R-ma$73r!}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
