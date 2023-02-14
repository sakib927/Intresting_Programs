import random
i = 1
while i<10:
  print()
  print(f"You are at Level {i}")
  print()
  if i<=0:
    print("Improve your math")
    break
  for j in range(0,3):
    a = random.randint(10**(i-1),10**(i))
    b = random.randint(10**(i-1),10**(i))
    print(f"Add {a} and {b}",a+b)
    unum = int(input("Enter the value "))
    if unum == a+b :
      print("done")
      i = i+1
      break
    else:
      if j == 2:
        i = i-1
        break
      print("wrong")
