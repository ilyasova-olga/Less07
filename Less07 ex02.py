from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def my_method_1(self):
        print("Тип одежды:", end=' ')

    @abstractmethod
    def my_method_2(self):
        print("Параметры одежды:", end=' ')

    @abstractmethod
    def my_method_3(self):
        print("Расход ткани:", end=' ')


class Coat (Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Пальто")

    def my_method_2(self):
        super().my_method_2()
        print("Размер")

    def my_method_3(self):
        super().my_method_3()
        return float(self.value) / 6.5 + 0.5


class Suit (Clothes):
    def my_method_1(self):
        super().my_method_1()
        print("Костюм")

    def my_method_2(self):
        super().my_method_2()
        print("Рост")

    def my_method_3(self):
        super().my_method_3()
        return 2 * float(self.value) + 0.3


class Total:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return (self.a / 6.5 + 0.5) + (2 * self.b + 0.3)


size_coat = 1
size_suit = 1

print("\n")
c = Coat(size_coat)
c.my_method_1()
c.my_method_2()
print("%.2f" % c.my_method_3())


print("\n")
s = Suit(size_suit)
s.my_method_1()
s.my_method_2()
print("%.2f" % s.my_method_3())


t = Total(size_coat, size_suit)
print("Общий расход ткани: %.2f" % t.sum())