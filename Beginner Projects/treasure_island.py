print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
first = input("You are at a cross road. Where do you want to go? Type 'L' for left and 'R' for right. ")
if (first.lower()) == 'r':
          print("You have fallen into a hole!! Game over :(((")

else:
          second = input("You have arrived at a lake. Far ahead, you see that there is an island. Type 'wait' to wait for a boat, or 'swim', to swim across the lake. ")
          if second.lower() == "swim":
                    print("You are being attacked by a trout!!! Game over :(((")
          else:
                    third = input("You have reached the island. There are 3 doors infront of you; red, blue and yellow. Which door has a treasure behind it?")
                    if third.lower() == 'red':
                              print("You got burned by fire! Game over!!")
                              
                    elif third.lower() == 'blue':
                              print("You were eaten by beasts!. Game over!!")
                    elif third.lower() == 'yellow':
                              print("You won!!")
                    else:
                              print("Game over!!")
                    
