# To guess number from 1 to 100
import random as r
n = r.randint(1,100)
print("Guess the number from 1 to 100!")
guesses = 0
a = -1
while(a != n):
    # Only guess is moved to the top!!
    guesses += 1
    a = int(input("Guess the number: "))
    
    if(n<a):
        print("Lower number please")
        
    else:
        print("Higher number please")

print(f"You have guessed the correct number ({n}) in {guesses} attempts.")
