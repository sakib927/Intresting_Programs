import random
round = 0
score2 = 0
score1 = 0
flag_again = 0

def movie_game():
  movie_list = ["3idiots","Pathan","Baahubali","Dangal","KGF"]
  movie = movie_list[random.randint(0,len(movie_list)-1)]
  movie = movie.lower()
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
      positive_point = 0
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
      positive_point = 1
      print("You did it!!")
      break

  return positive_point

def score_board(score1,score2):
  print(f"The Points achived by Player 1 is {score1} and Player 2 is {score2}")
  if score2>score1:
    print("Player 2 wins")
  elif score2<score1:
    print("Player 1 wins")
  else:
    print("Both have achived tie so you can play this once more or else you can maintain this tie score and exit")
    print("Enter 0 to contiue or press 1 to exit")
    tie_option = int(input("Enter your choice"))
    score1 = 0
    score2 = 0
    if tie_option == 0:
      flag_again = 1
    else:
      flag_again = 0
  return flag_again

while True:
  print()
  if round == 2 and flag_again == 0:
    tie_do = score_board(score1,score2)
    if tie_do == 1:
      round = 0
    else :
      break

  if round%2 == 0:
    print("Welcome Player 1")
    m = movie_game() 
    score1 = score1 + m
    round = round +1
  else:
    print("Welcome Player 2")
    n = movie_game()
    score2 = score2 + n 
    round = round + 1
