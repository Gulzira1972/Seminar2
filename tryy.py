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




