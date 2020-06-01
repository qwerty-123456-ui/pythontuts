#modify guessing game
import random
win=random.randint(1,100)
a=True
c=0
while a:
    guess=int(input("Enter ur guess: "))
    c+=1
    if guess==win:
        print("u won")
        a=False
    elif guess>win:
        print("too high")
    else:
        print("too low")
print(f"u took {c} chances to win")