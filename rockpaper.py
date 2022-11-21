import random
user_score=0
while user_score<5 :
    uinput=input("enter your choice rock  paper or scissor: ")
    user_input=uinput.lower()
    choices=["rock","paper","scissor"]
    comp_choice=random.choice(choices)
    if(user_input==comp_choice):
        print("its a tie we got same objects he he he......")
        print("your score is ",user_score,"you just need 5 correct guesses to win the game")
        break
    elif(user_input=="rock"and comp_choice=="paper"):
        print("ooo....computer paper has grap your rock and unfortunately it died")
        print("your score is ",user_score,"you just need 5 correct guesses to win the game")
        break
    elif(user_input=="paper"and comp_choice=="scissor"):
        print("ooo....computer Scissor has sliced your paper and unfortunately it died")
        print("your score is ",user_score,"you just need 5 correct guesses to win the game")
        break
    elif(user_input=="scissor"and comp_choice=="rock"):
        print("ooo....computer rock has breaked your Scissor and unfortunately it died")
        print("your score is ",user_score,"you just need 5 correct guesses to win the game")
        break
    elif(comp_choice=="rock"and user_input=="paper"):
        print("ooo....your paper has grap computers rock and unfortunately it died")
        user_score+=1
        print("your score is ",user_score,"you just need",5-user_score,"correct guesses to win the game")
        break
    elif(comp_choice=="paper"and user_input=="scissor"):
        print("ooo....computer Scissor has sliced your paper and unfortunately it died")
        user_score+=1
        print("your score is ",user_score,"you just need",5-user_score,"correct guesses to win the game")
        break
    elif(comp_choice=="scissor"and user_input=="rock"):
        print("ooo....computer rock has breaked your Scissor and unfortunately it died")
        user_score+=1
        print("your score is ",user_score,"you just need",5-user_score,"correct guesses to win the game")
        break
else:
    print("conguratulations you won")
   





