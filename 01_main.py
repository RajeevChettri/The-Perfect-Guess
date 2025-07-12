# To guess number from 1 to 100
import random as r
n = r.randint(1,100)
print("Guess the number from 1 to 100!")
guesses = 0
a = -1
while(a != n):
    a = int(input("Guess the number: "))
    
    if(n<a):
        print("Lower number please")
        guesses += 1
        
    else:
        print("Higher number please")
        guesses +=1

print(f"You have guessed the correct number ({n}) in {guesses} attempts.")