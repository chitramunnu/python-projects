import random
def guessNumber(x):
    random_number = random.randint(1, x)
    guess = 0 
    while guess != random_number:
        guess = int(input(f'guess the number between 1 and {x}:'))
        if guess < random_number:
            print('too high guess again')
        elif guess > random_number:
            print('too low guess again')
    print('you have guessed the number')
guessNumber(10)
        
    
