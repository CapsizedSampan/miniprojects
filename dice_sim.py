print("**start dice sim**")

#import the stuff
from random import seed
from random import randint

#choose dice type
print("dice types: \n1. normal(6-sided dice)\n2. 8-sided dice \n3. custom")
while True:
    dice_type = input("choose dice type(enter number): ")
    if dice_type == '1':
        sec = 6
        break
    elif dice_type == '2':
        sec = 8
        break
#custom dice: need to be an integer. else, quit
    elif dice_type == '3':
        maxno = input('Enter max. number')
        try:
            sec = int(maxno)
        except:
            print('Invalid input')
            quit()
        break
    else:
        print('Invalid input')
        continue

#seed random no. generator
def roll_dice(a,b):
    print(randint(a,b))

num = 0
seed(1)
while True:
    user = input("Roll dice?(yes/no)\n")
    if user == 'yes':
#roll dice!!
        first = 1
        roll_dice(first,sec)
    elif user == 'no':
        break
    else:
        print("Invalid input")
        continue

print("**end dice sim**")
