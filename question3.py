principle = float(input("Enter principle: "))
years = int(input("Enter years: "))
if principle > 100000:
  rate = 0.06
  intrest = principle * rate
elif principle >= 50000 and principle <= 100000 and years == 10:
  rate = 0.05
  intrest = principle * rate
elif principle >= 50000 and principle <= 100000 and years == 5:
  rate = 0.04
  intrest = principle * rate
else:
  rate = 0.02 
  intrest = principle * rate
print(f"Principle: ${principle} \nInterest rate: %{rate*100} \nInterest after one year: ${intrest}")