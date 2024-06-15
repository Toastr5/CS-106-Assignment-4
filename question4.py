quantity = int(input("Enter quantity: "))
if quantity >= 25:
  cost = 50
  total = cost * quantity
elif quantity <= 24 and quantity >= 10:
  cost = 60
  total = cost * quantity
elif quantity <= 9 and quantity >= 5:
  cost = 70
  total = cost * quantity
else:
  cost = 75
  total = cost * quantity
print(f"Number of tickets: {quantity} \nCost per ticket: ${cost} \nTotal cost: ${total}")