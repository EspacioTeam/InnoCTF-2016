#!/bin/python

def grade(arg, key):
    if "InnoCTF{d0nt_fOrg3t_t0_35c4p3_qu3ri3s}" == key:
        return True, "Флаг принят"
    else:
        return False, "Неверный флаг"
