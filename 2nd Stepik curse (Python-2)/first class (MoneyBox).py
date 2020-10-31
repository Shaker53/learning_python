class MoneyBox:
    def __init__(self, capacity):
        self.money = 0
        self.capacity = capacity

    # конструктор с аргументом – вместимость копилки

    def can_add(self, v):
        return self.money + v <= self.capacity
    # True, если можно добавить v монет, False иначе

    def add(self, v):
        self.money += v
    # положить v монет в копилку


pig = MoneyBox(50)
print(pig.can_add(100))
pig.add(20)
print(pig.money)
print(pig.can_add(40))
print(pig.can_add(20))
print(pig.can_add(30))
pig.add(25)
print(pig.money)