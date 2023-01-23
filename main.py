# Каждая копилка имеет ограниченную вместимость, которая выражается целым числом
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        # if self.capacity % 1 == 0 and self.capacity >= 1:
        #    self.capacity = capacity
        #    self.count = 0
        # else :
        #    print("введите целое число вместимости монет и больше 0")
# конструктор с аргументом – вместимость копилки
    def can_add(self, v):
        if self.capacity - v >= 0 and self.count + v < self.capacity:
            can_to_add = True
        else:
            print("не вмещается столько монет, укажи меньше")
            can_to_add = False
# True, если можно добавить v монет, False иначе
    def add(self, v):
        self.count += v

x = MoneyBox(5)
print(x.count)
x.add(3)
print(x.count)
x.can_add(4)
print(x.count)
# положить v монет в копилку