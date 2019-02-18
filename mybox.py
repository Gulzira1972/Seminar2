from myclass import Tortbyrish

class MyBox(Tortbyrish):
       def __init__(self,):
           self._tort=list()
           
       def __len__(self):
          return len(self.Tortbyrish)
          
       def add(self,b):
           self.Tortbyrish.append(b)
           
       def remove(self, width):
            assert width in self._tort
            idx=self._tort.index(width)
            return self._tort.pop(idx)

       def __contains__ (self, color):
            return color in self._tort

       def __iter__(self, width):
            return MyBox(self._tort)
print('eto iz MyBox')


