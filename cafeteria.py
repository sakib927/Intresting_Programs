def cafeteria():
  print("Welcome To Aamir Dhaba")
  print()
  print("Here is the menu")
  menu = {"FriedRice":130,"Dhosa":100,"JeraRice":70,"Dal":60,"SoftDrink":50}
  for i,j in menu.items():
    print(i,"and its price",j)
  print()
  j = 1
  for i in menu.keys():
    print("Press",j,"for ",i)
    j += 1

  print()
  print("We will Start taking your order")
  print("You may press 0 for quiting")

  def order_list(d1):
    for i,j in d1.items():
      if i == 1:
        print('FriedRice in',j,"quantity")
      elif i == 2:
        print("Dhosa in",j,"quantity")
      elif i == 3:
        print("JeraRice",j,"quantity")
      elif i == 4:
        print("Dal",j,"quantity")
      elif i == 5:
        print("SoftDrink",j,"quantity")


  d1 = {}

  while True:
    print()
    user_input_choice = int(input("Enter Your choice "))
    if user_input_choice == 0 or user_input_choice == ""  :
      print()
      order_list(d1)
      print()
      print("Do you want to edit your order")
      print("Yes for editing or No for exiting")
      print()
      user_last_input = input("Enter Your choice")
      user_last_input.lower()
      if user_last_input == "no" or user_last_input =="": 
        break
      elif user_last_input == "yes" or user_last_input !="" or user_last_input!="no" :
        user_input_choice = int(input("Enter Your choice "))
        if user_input_choice == 0 or user_input_choice == ""  :
          break
        user_input_quantity = int(input("Enter no of quantity "))
        if user_input_quantity == 0 or user_input_quantity == "":
          user_input_quantity = 1
        d1[user_input_choice] = user_input_quantity
      else:
        print("invalid")

    else:  
      user_input_quantity = int(input("Enter no of quantity "))
      if user_input_quantity == 0 or user_input_quantity == "":
        user_input_quantity = 1
      d1[user_input_choice] = user_input_quantity


  cart = []
  price = []


  for i,j in d1.items():
    if i == 1:
      cart.append('FriedRice')
      price.append(menu['FriedRice']*j)
    elif i == 2:
      cart.append("Dhosa")
      price.append(menu["Dhosa"]*j)
    elif i == 3:
      cart.append("JeraRice")
      price.append(menu["Dhosa"]*j)
    elif i == 4:
      cart.append("Dal")
      price.append(menu["Dal"]*j)
    elif i == 5:
      cart.append("SoftDrink")
      price.append(menu["SoftDrink"]*j)

  print()
  print("Order invoice ")
  print()
  finalprice = sum(price)
  order_list(d1)
  print("Your final total is ",finalprice)

cafeteria()
