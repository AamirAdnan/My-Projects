#Dice game..........
import random
print("Ladies and gentelmen welcome to my virtual Dice  ")
print("so without wasting any time lets start the game of Dice")
while True:
    choose=input("Do you want to roll a dice print Y for yes and N for no")
    if choose.lower() == "y":
        number=random.randint(1,6)
        print("your dice number is.......",number)
    elif choose.lower() =="n":
        print("Thanks for playing with us Hope you have a beautiful day Ahead")
    else:
        print("please select y or n ")




