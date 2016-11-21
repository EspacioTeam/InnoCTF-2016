#!/usr/bin/python3

def grade(arg, key):
    flag = "InnoCTF{05fe6d8bb61f9115b672e73282e0cda7}"
    if flag in key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"