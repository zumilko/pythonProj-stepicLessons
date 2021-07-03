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

decode, code, str_code, str_decode = [input() for i in range(4)]
cipher = dict(zip(decode, code))  # словарь для кодирования, склеивается из 2х списков или строк! поэлементно
# переворачивание словаря как то так {v: k for k, v in dict_.items()}:
decode_cipher = {cipher: k for k, cipher in cipher.items()}  # словарь для декодирования
# print(f"{code}\n{decode}\n{cipher}\n{decode_cipher}")
for a in str_code:
    print(cipher[a], sep = '', end = '')
print()
for b in str_decode:
    print(decode_cipher[b], sep = '', end = '')