class ThreeValues(object):
    def __init__(self, value1, value2, value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def __repr__(self):
        return "ThreeValues: %s,%s,%s" % (self.value1, self.value2, self.value3)


class MyPoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "MyPoint: %s,%s" % (self.x, self.y)
