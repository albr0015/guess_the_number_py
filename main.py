import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while (guess != random_number):
        guess = int(input(f'Guess a number 1 to {x}\n'))

        if guess < random_number: 
            print('Too low.')
        elif guess > random_number: 
            print('Too high')

    print(f'You win, random number is {random_number}')

def computer_guess(x):
    low = 1 
    high = x 
    feedback = ""

    while feedback != 'c':
        if low != high:
            guess=random.randint(low,high)
        else: 
            guess = low 
             
        feedback=input(f'Is {guess} too high(H), too low (L), or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess +1

    print(f'The computer gussed your number, {guess}, is the number!')

    
