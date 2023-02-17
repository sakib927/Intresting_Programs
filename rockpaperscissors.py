computerl = ["rock","paper","scissors"]
computer_choice = computerl[random.randint(0,len(computerl)-1)]
computer_choice

print("Welcome to Rock Paper Sissors")
print("Computer Vs User")
print()
print("Press r for Rock")
print("Press p for Paper")
print("Press s for Scissors")
print()
user_intput = input("Enter your choice ")
user_intput = user_intput.lower() 
print()
print(f"The Computer Entered {computer_choice}")
print()

if (computer_choice == "rock" and user_intput=="r") or (computer_choice == "paper" and user_intput=="p") or computer_choice == "sissors" and user_intput=="s":
  print("Tie")
elif (computer_choice == "rock" and user_intput == "p") or (computer_choice == "paper" and user_intput == "r"):
  if computer_choice == "rock":
    print("User Won")
  else:
    print("Computer Won")
elif (computer_choice == "rock" and user_intput == "s") or (computer_choice == "scissors" and user_intput == "r"):
  if computer_choice == "scissors":
    print("User Won")
  else:
    print("Computer Won")
elif (computer_choice == "paper" and user_intput == "s") or (computer_choice == "scissors" and user_intput == "p"):
  if computer_choice == "paper":
    print("User Won")
  else:
    print("Computer Won")
else:
  print("Invalid")
  print("Computer Won by Default")
