
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.z = 1

    def dist(self, obj):
        return sqrt((self.x - obj.x)**2 + (self.y - obj.y)**2)
