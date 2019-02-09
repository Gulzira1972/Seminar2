class Tortbyrish:
   def __init__(self, color="blue", width=100, height=100):
       self.color = color
       self.width = width
       self.height = height

   def audan(self):
       return self.width * self.height
rect1 = Tortbyrish()
print(rect1.color)
print(rect1.audan())
rect1 = Tortbyrish("white", 23, 34)
print(rect1.color)
print(rect1.audan())
