# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный),
# name - индивидуальное название каждого животного.
class Animal:
    alive = True  # Живой
    fed = False  # Накормленный

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible == True:
            self.fed = True
            print(f'{self.name} съел {food.name}')
        else:
            self.alive = False
            print(f"{self.name} не стал есть {food.name}")


# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
class Mammal(Animal):  # Млекопитающее
    pass


# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
class Predator(Animal):  # Хищник
    pass


# Для класса Plant атрибут
# edible = False(съедобность),
# name - индивидуальное название каждого растения
class Plant:
    edible = False      # edible (съедобность)

    def __init__(self, name):
        self.name = name


class Fruit(Plant):
    edible = True      # (переопределить при наследовании), edible (съедобность)


class Flower(Plant):
    edible = False     # (переопределить при наследовании), edible (съедобность)
     


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
