import abc
from models import Cow, Chicken

"""オブジェクト作成時に、作成するオブジェクトのクラスをサブクラスに選ばせる"""


class Factory(metaclass=abc.ABCMeta):
    def __init__(self, ):
        self.animal = self.factory_method()

    def check_animal(self):
        self.animal.eat()

    @abc.abstractmethod
    def factory_method(self):
        pass


class CowFactory(Factory):
    def factory_method(self):
        return Cow()


class ChickenFactory(Factory):
    def factory_method(self):
        return Chicken()


if __name__ == '__main__':
    cow = CowFactory()
    cow.check_animal()

    print("*" * 100)
    chicken = ChickenFactory()
    chicken.check_animal()
