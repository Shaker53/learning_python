import json


def finding_all_sons(parents):
    sons = []
    for parent in parents:
        sons += dict_inheritans[parent]
    if len(sons) == 1:
        return set(sons + list(finding_all_sons(sons)))
    elif len(sons) > 1:
        return set(sons + list(finding_all_sons_n_args(sons)))
    else:
        return set(list(sons))


def finding_all_sons_n_args(parents):
    sons = []
    for parent in parents:
        sons += dict_inheritans[parent]
    if len(sons) == 1:
        return set(sons + list(finding_all_sons(sons)))
    elif len(sons) > 1:
        return set(sons + list(finding_all_sons_n_args(sons)))
    else:
        return set(list(sons))


data_json = input()
data_py = json.loads(data_json)
dict_inheritans = {}
dict_all_sons = {}
for row in data_py:
    if row['name'] not in dict_inheritans:
        dict_inheritans[row['name']] = []
        dict_all_sons[row['name']] = []
    for i in row['parents']:
        if i not in dict_inheritans:
            dict_inheritans[i] = []
            dict_all_sons[i] = []
for row in data_py:
    for i in row['parents']:
        dict_inheritans[i].append(row['name'])

for i in sorted(dict_inheritans.keys()):
    print(i, ':', len(finding_all_sons([i])) + 1)


"""Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

﻿Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
"""
