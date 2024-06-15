part_number = int(input("Input part number: "))
quantity = int(input("Input quantity: "))
if part_number == 10 or part_number == 55:
  unit_cost = 1.00
  total = quantity * unit_cost
elif part_number == 99:
  unit_cost = 2.00
  total = quantity * unit_cost
elif part_number == 80 or part_number == 70:
  unit_cost = 3.00
  total = quantity * unit_cost
else:
  unit_cost = 5.00
  total = quantity * unit_cost
print(f"For part {part_number} at ${unit_cost} per unit, for"
      f" a total of {quantity} units, the cost is ${total}")
