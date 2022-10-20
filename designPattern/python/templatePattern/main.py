import abc
import sys
import models

"""
Template Methodsのパターン
処理の枠組みを決める。
"""


class TestFrame(metaclass=abc.ABCMeta):
    def __init__(self):
        self.counter = 0

    @abc.abstractmethod
    def setup(self):
        pass

    @abc.abstractmethod
    def main(self):
        pass

    @abc.abstractmethod
    def teardown(self):
        pass

    def test(self):
        self.setup()
        try:
            self.main()
        except AssertionError:
            self.counter += 1
            sys.stderr.write("E => {}".format(self.__class__.__name__))
        if self.counter == 0:
            sys.stderr.write(". => {}".format(self.__class__.__name__))
        self.teardown()


if __name__ == '__main__':
    models.Test1().test()
    models.Test2().test()
