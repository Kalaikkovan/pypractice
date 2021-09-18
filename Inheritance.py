class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Animal generally makes noise')


class Dog(Animal):
    def __init__(self, name) -> object:
        self.name = name

    def speak(self):
        print('This dog named {} will bark'.format(self.name))


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print('Cat names {} will make sound like Meow!'.format(self.name))


myDog = Dog('Puppy')

myDog.speak()
myCat = Cat('Pussy')
myCat.speak()
