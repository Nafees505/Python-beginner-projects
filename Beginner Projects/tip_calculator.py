print("Welcome to the tip calculator!\n")
total = float(input("What was the total bill? "))
tip = int(input("What % of tip do you want to give? 10, 12 or 15? "))
num_of_people = int(input("How many people you want to split the bill with? "))
price_for_each = round((total+((total/100)*tip))/num_of_people, 2)
print(f"Each person should pay: {price_for_each}")
