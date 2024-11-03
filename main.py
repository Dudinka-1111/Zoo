#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
#(например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.

class Animal():
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает.")

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
#которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется
#(например, различный звук для `make_sound()`).

class Bird(Animal):
    def _init_(self, species, color):
        self.species = species
        self.color = color

    def make_sound(self):
        print('Птицы поют')

class Mammal(Animal):
    def _init_(self, habitat, size):
        self.habitat = habitat
        self.size = size

    def make_sound(self):
        print('Млекопитающие издают разные звуки')

class Reptile(Animal):
    def _init_(self, venomous, locomotion):
        self.venomous = venomous
        self.locomotion = locomotion

    def make_sound(self):
        print('Рептилии шипят, скрипят и т.д.')

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
#которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

animals = [Bird(), Mammal(), Reptile()]
for animal in animals:
    animal.make_sound()

#4. Используйте композицию для создания класса `Zoo`,
#который будет содержать информацию о животных и сотрудниках.
#Должны быть методы для добавления животных и сотрудников в зоопарк.

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное в зоопарк: {animal}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен сотрудник в зоопарк: {employee}")

    def list_animals(self):
        print("Животные в зоопарке:")
        for animal in self.animals:
            print(f"- {animal}")

    def list_employees(self):
        print("Сотрудники зоопарка:")
        for employee in self.employees:
            print(f"- {employee}")


# Пример использования
zoo = Zoo()

# Добавляем животных
zoo.add_animal('Лев')
zoo.add_animal('Тигр')

# Добавляем сотрудников
zoo.add_employee('Иван Иванов')
zoo.add_employee("Анна Петрова")

# Выводим списки животных и сотрудников
zoo.list_animals()
zoo.list_employees()

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
#которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()`
#для `Veterinarian`).

class Employee:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Employee):
    def __init__(self, name):
        super().__init__(name)

    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal}.")

class Veterinarian(Employee):
    def __init__(self, name):
        super().__init__(name)

    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal}.")

# Пример использования классов
zookeeper = ZooKeeper('Иван Иванов')
veterinarian = Veterinarian('Анна Петрова')

zookeeper.feed_animal("льва")
veterinarian.heal_animal("тигра")

#Дополнительно:
#Попробуйте добавить дополнительные функции в вашу программу,
#такие как сохранение информации о зоопарке в файл и возможность её загрузки,
#чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import pickle

def save_zoo(zoo, filename):
    with open(filename, 'wb') as f:
        pickle.dump(zoo, f)
    print("Файл Zoo сохранен.")

def load_zoo(filename):
    with open(filename, 'rb') as f:
        zoo = pickle.load(f)
    print("Файл Zoo загружен.")
    return zoo

# Пример использования
save_zoo(zoo, 'zoo_data.pkl')
loaded_zoo = load_zoo('zoo_data.pkl')