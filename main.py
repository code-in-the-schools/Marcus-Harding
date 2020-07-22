import random
r =random.randit(-100,100)

found = False
while found == False
a = int(input("Guess a number "))

if a == r:
  found = True
  print("winner!!")
  elif a>r:
    print(str(a), "is more than ")
    elif a<r:
      print(str(a), "is less than ")
      else:
        print("This is not a number, try again.")