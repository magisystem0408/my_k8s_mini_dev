import abc


class WeatherState(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def umbrella(self):
        raise NotImplementedError("umbrella is abstractmethod")

    @abc.abstractmethod
    def laundry(self):
        raise NotImplementedError("laundry is abstractmethod")


class SunnyDay(WeatherState):
    def umbrella(self):
        print("bring no umbrella")

    def laundry(self):
        print("dry outdoor")


class CloudyDay(WeatherState):
    def umbrella(self):
        print("bring folding umbrella")

    def laundry(self):
        print("bring indoor")


class RainyDay(WeatherState):
    def umbrella(self):
        print("bring normal umbrella")

    def laundry(self):
        print("dry indoor")
