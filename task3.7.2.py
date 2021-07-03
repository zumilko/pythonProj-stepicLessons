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

input_data = [input() for i in range(4)]
cipher = dict(zip(input_data[0], input_data[1]))
code = [i for i in input_data[2]]
decode = [i for i in input_data[3]]
print(f"{code}\n{decode}\n")
print([cipher[a] for a in code])
# переворачивоние словаря: {v: k for k, v in dict_abc.items()}
decode_cipher = {cipher: k for k, cipher in cipher.items()}
print([decode_cipher[b] for b  in decode])