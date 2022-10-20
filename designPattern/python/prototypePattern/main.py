import copy

"""
オブジェクトをコピーすることでオブジェクトを作る
"""


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    point = Point(2, 4)
    point2 = copy.deepcopy(point)

    print("x", point.x, point2.x)
    print("y", point.y, point2.y)


