SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

class Object:

    def print_fuc(self):
        print(self.x, self.y, self.width, self.height)

class Ship(Object):
    def __init__(self):
        self.width = 30
        self.height = 30


a = Ship()
print(a.x)
