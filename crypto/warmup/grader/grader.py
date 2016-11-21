#!/usr/bin/python3
def grade(arg, key):
    flag = "InnoCTF{226246784982996043258925535013949890369}"
    if flag in key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"