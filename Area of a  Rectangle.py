class Rectangle:
    def __init__(self,l ,w) :
        self.length = l
        self.width = w
    def Rectangle_area(self):
        return self.length * self.width
newRectangle = Rectangle(12, 10)
print("Dimensions of rectangle -length: %d width: %d"%(newRectangle.length, newRectangle.width))
print("Area of rectangle:",newRectangle.Rectangle_area())
