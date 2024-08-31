def buy(chocolates):
    name = input("Enter the name of the chocolate :")
    quantity = int(input("Enter the quantity of the chocolate :"))
    amount=0
    for chocolates in chocolates:
      if chocolates["name"] == name:
        if quantity<=chocolates["stock"]:
          amount = quantity*chocolates["amount"]
          chocolates["stock"]-=quantity
        else:
          print("out of stock")
    return chocolates,amount