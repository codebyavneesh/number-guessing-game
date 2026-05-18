print("\n=======NUMBER GUESSING GAME created by AVNEESH YADAV=======\n")

import random

secret_number = random.randint(1, 100)

attampts = 0
while True:
    try:
        user_guess = int(input("Enter your guess number: "))
    except ValueError:
        print("Please Enter a Valid Number !!")
        continue
    
    if user_guess<1 or user_guess>100:
        print("Error: Number should be 1 to 100 !!")
        continue
    
    attampts += 1
    
    if user_guess < secret_number:
        print("Too low !! try again.\n")
    
    elif user_guess > secret_number:
        print("Too high !! try again.\n")
        
    else: 
        print(f"\nCorrect Answer !! you take {attampts} attampts.")
        break
        