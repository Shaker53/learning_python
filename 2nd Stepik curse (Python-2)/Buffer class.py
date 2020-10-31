class Buffer:
    def __init__(self):  # конструктор без аргументов
        self.list = []

    def add(self, *a):  # добавить следующую часть последовательности
        self.list += a
        while len(self.list) >= 5:
            print(sum(self.list[i] for i in range(5)))
            self.list = [self.list[j] for j in range(5, len(self.list))]  # обрезает первые пять элементов списка

    def get_current_part(
            self):              # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором
        return self.list        # они были
                                # добавлены


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6)
print(buf.get_current_part())
buf.add(7, 8, 9, 10)
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(buf.get_current_part())
