widget = int(input("Enter quantity of widgets: "))
if widget < 50000:
  unit_cost = 10
  cost = widget * unit_cost
elif widget <= 50000 and widget > 100000:
  unit_cost = 20
  cost = widget * unit_cost
else: 
  unit_cost = 30
  cost = widget * unit_cost
tax = round(cost * .07,2)
print(f"For a total of {widget} widgets at ${unit_cost} per unit, " 
f" the cost is ${cost} with taxes being ${tax} totals to ${tax + cost}")