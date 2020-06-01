import random
# winning_no=random.random() [range 0-1]
winning_no=random.randint(0,100)
# winning_no=7
guessed_no=float(input("Guess a number "))
if(guessed_no==winning_no):
    print("U WON ")
elif(guessed_no>winning_no):
    print("TOO HIGH")
else:
    print("TOO LOW")
print(winning_no)

