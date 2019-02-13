class MyBoxIterator:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a *= 2
      return x
    else:
      raise StopIteration

myclass = MyBoxIterator()
myiter = iter(myclass)

for x in myiter:
  print(x)
