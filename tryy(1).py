def call(n,m):
        n=13
        m=9
        print(n+m)
print("start")
try:
   val = int(input("input number: "))
   tmp = 10 / val
   print(tmp)
except Exception as e:
   print("Error! " + str(e))
print("stop")

try:
    num = int(input("input number: "))
    print("number:", num)
except:
    print("conversion failed")
print("stop")

try:
    call()
except:
    print('NotImplementedError')

  
