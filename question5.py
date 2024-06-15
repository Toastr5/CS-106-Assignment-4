name = str(input("Enter last name: "))
salary = float(input("Enter salary: "))
job_level = int(input("Enter job level: "))
if job_level >= 10:
  bonus_rate = 0.25
elif job_level >= 5 and job_level <= 9:
  bonus_rate = 0.20
else:
  bonus_rate = 0.10
bonus = salary * bonus_rate
print(f"Last name: {name} \n Bonus rate: {bonus_rate *100}% \nBonus: ${bonus}")