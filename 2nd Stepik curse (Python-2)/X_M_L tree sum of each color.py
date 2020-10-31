from xml.etree import ElementTree


def colors_of_sons(element, value=1):
    dict[element.attrib['color']] += value
    for child in element:
        colors_of_sons(child, value=value + 1)


dict = {'red': 0, 'green': 0, 'blue': 0}
root = ElementTree.fromstring(input())
colors_of_sons(root)
for i in ['red', 'green', 'blue']:
    print(dict[i], end=' ')

"""
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue﻿).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1. Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:

<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>
Sample Output:

4 3 1
"""
