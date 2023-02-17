import random 

def rolldice():
  num = random.randint(1,6)
  return num 

snake_ladder={1:38,4:14,8:10,21:42,28:74,50:67,71:92,80:99,97:78,95:56,88:24,62:18,36:6,48:26,32:10}
position = 0
print("Welcome to Snake and Ladder ")
while True:
  if position == 100:
    print("Winner")
    break
  print()
  print("Press 1 to roll the dice")
  user_input = int(input("Enter your choice "))
  print()
  if user_input == 1:
    dicenum = rolldice()
    print("The dice has shown ",dicenum)
    position += dicenum
    if position > 100:
      position -= dicenum
  else:
    print("Invalid choice")

  print("You are currently in ",position,"position")
  for i,j in snake_ladder.items():
    if position == i:
      position = j
