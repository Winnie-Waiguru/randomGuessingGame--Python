import random

userGuess= input("Enter a number: ")


if userGuess.isdigit():
   userGuess= int(userGuess)
   
   if userGuess <= 0:
       print("Please input a number that is greater than 0")
       quit()
   else:
       print("Please input a number .") 
       quit()    

number= random.randint(0, userGuess)
print(number)