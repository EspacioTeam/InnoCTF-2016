#!/usr/bin/python3
def grade(arg, key):
	flag = "InnoCTF{e9d160f9699503d2555323034c725c23}"
	if flag in key:
		return True, "Флаг принят"
	else:
		return False, "Неверный флаг"