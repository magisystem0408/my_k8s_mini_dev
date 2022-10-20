"""
stateパターン
stateによって値を変える
"""
from weather import SunnyDay, CloudyDay, RainyDay


class Context(object):
    def __init__(self):
        self.sunny = SunnyDay()
        self.rainy = RainyDay()
        self.cloudy = CloudyDay()
        """初期値を入れる"""
        self.state = self.sunny

    def change_state(self, weather):
        if weather == "sunny":
            self.state = self.sunny
        elif weather == "rainy":
            self.state = self.rainy
        elif weather == "cloudy":
            self.state = self.cloudy
        else:
            raise ValueError("change_state method be in {}".format(["sunny", "rain", "cloud"]))


    def umbrella(self):
        self.state.umbrella()
    def laundry(self):
        self.state.laundry()


if __name__ == '__main__':
    state = Context()
    state.umbrella()
    state.laundry()

    print("*" * 10 + "プロセス2" + "*" * 10)

    state.change_state("rainy")
    state.umbrella()
    state.laundry()

    print("*" * 10 + "プロセス2" + "*" * 10)

    state.change_state("cloudy")
    state.umbrella()
    state.laundry()




