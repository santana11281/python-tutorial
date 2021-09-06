class Cookie:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        print(self.color)
        return self.color


    def setColor(self, color):
        self.color = color


cookie_one = Cookie("blue")
cookie_two = Cookie("red")

cookie_one.setColor("black")

cookie_one.getColor()

