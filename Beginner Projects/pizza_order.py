print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
final = 0
if size == "S":
  final += 15
  if add_pepperoni == "Y":
    final += 2
  if extra_cheese == "Y":
    final += 1
  
elif size == "M":
  final+=20
  if add_pepperoni == "Y":
    final += 3
  if extra_cheese == "Y":
    final += 1
else:
  final+=25
  if add_pepperoni == "Y":
    final += 3
  if extra_cheese == "Y":
    final += 1

print(f"Your final bill is: ${final}.")