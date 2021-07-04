"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках
указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the

"""

good = {input().lower() for j in range(int(input()))}
test = [input().lower().split() for j in range(int(input()))]
test_w = {elm for lst in test for elm in lst}
err_word = test_w - good
print(*err_word, sep='\n')
# перевести вложенный список в плоский, мой вымученный вариант:
# for lst in test:
#     for elm in lst:
#         test_w = elm.split()
# подсмотрел https://habr.com/ru/post/63539/ :
# test_w=[]
# for lst in test:
#     test_w.extend(lst)
