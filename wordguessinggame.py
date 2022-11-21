import random
words=["python","java","c++","apple","mango","banana","microsoft","google","infoses","water"]
random_word=random.choice(words)
print("hint:the anwer is one of this word good luck",words)
print("******************************Word Guessing Game********************************************")
user_guess=""
chances=5
while chances>0:
    wrong_guesses=0
    for character in random_word:
        if character in user_guess:
            print("conguratulations you got the correct word which is=",character)
        else:
            wrong_guesses+=1
    if wrong_guesses==0:
        print("correct")
        print("word:",random_word)    
        break
    guess=input("Guess a word")
    user_guess+=guess
    if guess not in random_word:
        chances-=1
        print("wrong guess you have",chances," remaining")
        if chances==0:
            print("game over.Better Luck next Time")
            break

            