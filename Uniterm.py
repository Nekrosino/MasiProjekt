
class Uniterm:
    def __init__(self,x,y,czcionka):
        self.x = x
        self.y = y
        self.czcionka = czcionka


        def draw(self, canvas, dx=0, dy=0,tag="Empty"):
            raise NotImplementedError("Podklasa musi zaimplementowac funkcje draw()")