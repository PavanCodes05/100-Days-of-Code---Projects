print("Welcome to the tip calculator")

total = float(input("what was the total bill? "))
tip = int(input("How much tip would you like to give? (in %)? "))
people = int(input("How many people to split the bill? "))

tip_cal = (total / 100) * tip
final = total + tip_cal

print(f"Each person should pay {round(final/people, 2)}")