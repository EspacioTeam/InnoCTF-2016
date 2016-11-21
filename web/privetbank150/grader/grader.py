#!/usr/bin/python3

def grade(arg, key):
    flag = "InnoCTF{csrf_exploitation_has_never_been_so_easy}"
    if flag in key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"