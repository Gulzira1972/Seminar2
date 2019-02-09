from myclass import Tortbyrish

class MyBox:
       def __init__(self,tort):
           self.tort=Tortbyrish()

           
       def __len__(self):
          return len(self.color)
          

       def __add__(self,b):
           self..append(b)
           self.b=5
           print(self.b)

       def __remove__(self, h):
            assert h in self.MyBox
            val=self.MyBox.val(h)
            return self.MyBox.pop(val)

       def __contains__ (self, w):
            return w in self.MyBox

       def __iter__(self, w):
            return MyBox(self.w)
            
