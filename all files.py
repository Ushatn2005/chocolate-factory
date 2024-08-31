chocolates = [
    {"name":"dairy milk","amount": 70,"stock":100},
    {"name":"5 star","amount": 10,"stock":50},
    {"name":"munch","amount": 20,"stock":30},
    {"name":"temptation","amount":100,"stock":10},
    {"name":"tic tac","amount":10,"stock": 20},
    ]
	
def display(chocolates):
    for chocolate in chocolates:
        print("Name:", chocolate['name']," Amount:", chocolate['amount']," Stock:", chocolate['stock'])

flag = True
while flag:
  print("-"*70)
  print("chocolate factory")
  print("-"*70)
  print("1. shopkeeper")
  print("2. customer")
  print("0. exit")
  print("-"*70)
  choice = int(input("enter your choice :"))
  if choice == 1:
    shopkeeper_flag = True
    while shopkeeper_flag:
      print("-"*70)
      print("shopkeeper")
      print("-"*70)
      print("1. add chocolates")
      print("2. remove chocolates")
      print("3. update amount")
      print("4. update stock")
      print("5. display chocolates")
      print("0. back")
      print("-"*70)
      shopkeeper_choice = int(input("enter your choice :"))
      if shopkeeper_choice == 1:
        chocolates=add_chocolates(chocolates)
      elif shopkeeper_choice == 2:
        chocolates=remove_chocolates(chocolates)
      elif shopkeeper_choice == 3:
        chocolates=update_amount(chocolates)
      elif shopkeeper_choice == 4:
        chocolates=update_stock(chocolates)
      elif shopkeeper_choice == 5:
        print("-"*70)
        display(chocolates)
        print("-"*70)
      elif shopkeeper_choice == 0:
        print("-"*70)
        print("back to main menu")
        print("-"*70)
        shopkeeper_flag = False
      else:
         print("-"*70)
         print("enter a valid number:")
         print("-"*70)
  elif choice == 2:
     customer_flag = True
     while customer_flag:
       print("-"*70)
       print("customer")
       print("-"*70)
       print("1. buy chocolates")
       print("2. display")
       print("0. back")
       print("-"*70)
       customer_choice = int(input("enter your choice :"))
       if customer_choice == 1:
         chocolates= buy(chocolates)
       elif customer_choice == 2:
        print("-"*70)
        display(chocolates)
        print("-"*70)
       elif customer_choice == 0:
         print("-"*70)
         print("back to main menu")
         print("-"*70)
         customer_flag = False
       else:
         print("-"*70)
         print("enter a valid number:")
         print("-"*70)
  elif choice == 0:
      print("-"*70)
      print("exit")
      print("-"*70)
      flag = False
  else:
    print("-"*70)
    print("enter a valid number:")
    print("-"*70)
