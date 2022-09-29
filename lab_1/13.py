class Animal:

    __name: str

    def __init__(self, name):
        self.__name = name
        print(f"An animal called {name} was born!")

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, name): self.__name = name

    def eat(self, foodName):
        print(f'{self.__name} is eating {foodName}...')

    def makeNoise(self):
        print(f'{self.__name}\'s saying grrrrhh...')

class Cat(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.color = color
        self.weight = weight

    def makeNoise(self):
        print('Meow!')

class Dog(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.color = color
        self.weight = weight
        print('A dog\'s just arrived')

    def makeNoise(self):
        print(f'{super().name}\'s saying woof...')


class StringVar:
    __value: str

    def __init__(self, value):
        self.__value = value
        print('StringVar variable has been instantiated: ', value)

    def set(self, value): self.__value = value

    def get(self): return self.__value

class Point:
    __x: float
    __y: float

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        print(f'x = {self.__x}\ty = {self.__y}')

    def setX(self, x): self.__x = x
    def getX(self): return self.__x
    def setY(self, y): self.__y = y
    def getY(self): return self.__y

# demo
if __name__ == "__main__":
    cat = Cat('Tom', 'Gray', 4)
    cat.makeNoise()

    animal = Animal('V')
    print('Animal\'s name is', animal.name)
    animal.name = 'David'
    animal.eat('apple')
    animal.makeNoise()

    strObj = StringVar('qwerty')
    print(strObj.get())
    strObj.set('abcdef')
    print(strObj.get())

    dog1 = Dog('Charlie', 'White', 10.5)
    dog1.name = 'Winston'
    print(dog1.name)
    dog1.makeNoise()
    dog1.eat('cookie')
    dog2 = Dog('Kot', 'Ginger', 9)
    dog2.name = 'Noah'
    print(dog2.name)
    dog2.makeNoise()
    dog2.eat('p**p')
