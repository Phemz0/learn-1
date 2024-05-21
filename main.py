import time
import random

array = ["Rock","Paper","Scissors"]
systemAnswer = random.choice(array)

print("Welocme to Rock Paper And Scissors")
time.sleep(1)


choice = str(input("Enter Rock, Paper of Scissors: "))
if(choice not in array):
    print("Invalid input, try again")
elif(choice == "Rock" and systemAnswer =="Paper" ):
    print(f"{systemAnswer}, you lose")
elif(choice == "Paper" and systemAnswer == "Scissors"):
    print(f"{systemAnswer}, you lose")
elif(choice == "Scissors" and systemAnswer == "Rock"):
    print(f"{systemAnswer}, you lose")
elif(choice == "Rock" and systemAnswer =="Scissors"):
    print(f"{systemAnswer}, you win")
elif(choice == "Paper" and systemAnswer =="Rock"):
    print(f"{systemAnswer}, you win")
elif(choice == "Scissors" and systemAnswer =="Paper"):
    print(f"{systemAnswer}, you win")    
