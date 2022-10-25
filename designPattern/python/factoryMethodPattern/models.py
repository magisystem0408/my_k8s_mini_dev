import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def speak(self):
        pass


class Cow(Animal):
    def eat(self):
        print("Cow!:eat")

    def speak(self):
        print("Cow!:speak")


class Chicken(Animal):
    def eat(self):
        print("Chicken!:eat")

    def speak(self):
        print("Chicken!:speak")
