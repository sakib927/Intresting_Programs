import random
movie_list = ["3idiots","Pathan","Baahubali","Dangal","KGF"]
movie = movie_list[random.randint(0,len(movie_list)-1)]
movie=movie.lower()
movie = movie.replace(" ","")

l1 = []
for i in (movie):
 l1.append(i)

l2 = []
for i in range(len(movie)):
  l2.append("*")
l = 0
flag = 0

while True:
  if flag == 3:
    print("You have lost all the chances")
    break

  print()
  print(l2)
  print()

  option = input("Enter your guess ")
  option = option.lower()
  if option == 0:
    print("Invalid")
    break

  if option not in l1:
    flag = flag +1
  
  if option in l1:
    count_occ = l1.count(option)
    for i in range(count_occ):
      indexofl1 = l1.index(option)
      while True:
        l1[indexofl1] = 0
        break
      l2[indexofl1] = option
  
  if "*" not in l2:
    print()
    print(l2)
    print("Congratulation!!")
    print("You did it!!")
    break
