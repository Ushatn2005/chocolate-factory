def add_chocolates(chocolates):
    name = input("Enter the name of the chocolate: ")
    amount = int(input("Enter the amount of the chocolate: "))
    stock = int(input("Enter the stock of the chocolate: "))
    chocolates.append({"name": name, "amount": amount, "stock": stock})
    return chocolates
	
def remove_chocolates(chocolates):
    name = input("Enter the name of the chocolate to remove: ")
    for chocolate in chocolates:
        if chocolate["name"] == name:
            chocolates.remove(chocolate)
    return chocolates
	
def update_amount(chocolates):
    name = input("Enter the name of the chocolate to update: ")
    amount = int(input("Enter the new amount of the chocolate: "))
    for chocolate in chocolates:
        if chocolate["name"] == name:
            chocolate["amount"] = amount
    return chocolates
	
def update_stock(chocolates):
    name = input("Enter the name of the chocolate to update: ")
    stock = int(input("Enter the new stock of the chocolate: "))
    for chocolate in chocolates:
        if chocolate["name"] == name:
            chocolate["stock"] = stock
    return chocolates
