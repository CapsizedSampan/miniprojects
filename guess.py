from random import randint
from random import seed

print('\n**GUESS THE NUMBER START***\n')

def guessing():
    tries = 0
    while True:
        #user's GUESS
        userguess = input ('Make a guess:')
        try:
            guess = int(userguess)
            if guess<1 or guess>100:
                print('Number is between 1 and 100, try again!')
                continue
        except:
            print('Invalid input, please enter a number')
            continue
        #check if guess is correct
        if guess == chosen:
            print('You guessed right! The number is',chosen)
            tries = tries + 1
            print('You tried',tries,'number of times')
            break
        elif guess > chosen:
            print('Too high, try again!')
            tries = tries + 1
            continue
        elif guess < chosen:
            print('Too low, try again!')
            tries = tries + 1
            continue


while True:
#choose a random number
    print('Choosing a number between 1 and 100...')
    chosen=randint(1,100)
    guessing()
#after guessing it right
    replay = input('Do you want to play again?(y/n)')
    while (replay == 'y' or replay == 'n'):
        if replay == 'y':
            break
        elif replay == 'n':
            print('\nThanks for playing!!\n**END OF GAME**\n')
            quit()
#replay yes!!
    continue
