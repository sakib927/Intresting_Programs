def input_l():
  l1 = []
  while True:
    x = input("Enter the element ")
    if x == "q":
      break
    l1.append(int(x))
  return l1

def len_l(a):
  i = 0
  while True:
    try:
      a[i]
      i = i+1
    except IndexError as e:
      break
  return(i)

def add_l(a):
  sum = 0
  for i in range(len_l(a)):
    sum = sum + a[i]
  return(sum)

def max_l(a):
  max = 0
  for i in range(len_l(a)):
    if max < a[i]:
      max = a[i]
  return(max)

def min_l(a):
  min = a[0]
  for i in range(len_l(a)):
    if min > a[i]:
      min = a[i]
  return(min)

def avg_l(a):
  avg = add_l(a)/len_l(a)
  return avg

print("Enter the list")
l1 = input_l()

while True:
  print()
  print("You have following option")
  print("Sum,Min,Max,Avg,Len")
  print("Enter q for exiting")
  print()
  option = input("Enter your option ")
  option = option.lower()
  if option == "sum":
    print("Sum of all elements is ",add_l(l1))
  elif option == "min":
    print("min element is ",min_l(l1))
  elif option == "max":
    print("max element is ",max_l(l1))
  elif option == "avg":
    print("avg value is ",avg_l(l1))
  elif option == "len":
    print("len of list is ",len_l(l1))
  elif option == "q":
    print("Thank you!!")
    print("Exiting !!")
    break
  else:
    print("Invalid option")
