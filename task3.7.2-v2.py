'''
Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
Программа принимает на вход две строки одинаковой длины, на первой строке записаны символы исходного алфавита,
на второй строке — символы конечного алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом,
и ещё одна строка, которую нужно расшифровать.
Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac

Sample Input 1:
abcd
*d%#
abacabadaba
#*%*d*%

Sample Output 1:
*d*%*d*#*d*
dacabac
'''


#  Copyright (c) 2021.  Eugene Primakov

def crypt(d, c, sc):
    cipher = dict(zip(decode, code))
    c = ''.join([cipher[a] for a in list(sc)])
    return c


def decrypt(d, c, sd):
    cipher = dict(zip(code, decode))
    d = ''.join([cipher[a] for a in list(sd)])
    return d


decode, code, str_code, str_decode = [input() for i in range(4)]
print(crypt(decode, code, str_code))
print(decrypt(decode, code, str_decode))
