from main import TestFrame


class Test1(TestFrame):
    def setup(self):
        print("Test1 class setup method")

    def main(self):
        print("Test1 class main method")
        assert 1 == 1

    def teardown(self):
        print("Test1 class teardown method")


class Test2(TestFrame):
    def setup(self):
        print("Test2 class setup method")

    def main(self):
        print("Test2 class main method")
        assert 1 == 3

    def teardown(self):
        print("Test2 class teardown method")
