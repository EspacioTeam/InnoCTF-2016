#!/bin/python

def grade(arg, key):
    if "InnoCTF{Unc13_54m_d035_th3_b35t_h3_c4n}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
