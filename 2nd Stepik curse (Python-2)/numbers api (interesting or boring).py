import requests

api_url = 'http://numbersapi.com/'
params = {
    'json': 'true',
    'default': 'No'
}

with open("/home/ilya/Desktop/test_input.txt") as inf:
    for line in inf:
        line = line.rstrip()
        res = requests.get(api_url + line + '/math', params= params)
        data = res.json()
        with open('/home/ilya/Desktop/test_output.txt', 'a') as ouf:
            if data['text'] != 'No':
                ouf.write('Interesting\n')
            else:
                ouf.write('Boring\n')

""" В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring
"""