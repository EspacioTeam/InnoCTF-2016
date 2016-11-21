#!/bin/python

def grade(arg, key):
    if "InnoCTF{nic3_tRy_t0_f1nd_5ql_1nj3cti0n}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
