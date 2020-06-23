import random

def end():
    print('Thanks for playing!!!')
    print('\n***GAME END***\n')

print('\n***GAME START: FIND THE TREASURE***\n')
#tell players what to do
print('In search of the treasure left by King Dodo, you chanced upon an old castle. Navigate your way in the castle using "north", "south", "east", or "west", and get out once you get it! ')
print('You can quit anytime by typing "quit". Good luck!')

#setup
rooms = {'entrance': {'name': 'Entry Way', 'east': 'bedroom', 'north': 'kitchen', 'west': 'bathroom',
        'text': 'The stone floors and walls are cold and mouldy.'},
    'kitchen': {'name': 'Kitchen', 'east': 'living', 'south': 'entrance', 'north': 'dining',
        'text': 'There are some old iron pots on the stove and wooden bowls. People probably prepared food here'},
    'living': {'name': 'Living Room', 'west': 'kitchen', 'south': 'bedroom','north': 'laundry',
    'text': 'There is an old sofa with floral patterns and a coffee table and some dark stains on the floor.'},
    'bedroom': {'name': 'Bedroom', 'north': 'living', 'west': 'entrance','south':'closet',
    'text': 'This is clearly a bedroom, but no one has slept there in a long time.'},
    'dining': {'name': 'Dining Room','east':'laundry', 'south': 'kitchen', 'west':'guest',
    'text':'There are some dusty fine china on a gothic wooden table. The wooden chair at the end of the table creaks as a gust of wind blows in.'},
    'bathroom':{'name':'Bathroom', 'east': 'entrance','text':'This is clearly an old bathroom for the rich. Water drips from the rusty copper faucet every few minutes.'},
    'laundry':{'name':'Laundry','west':'dining','south':'living','text':'There are some buckets and cleaning supplies in the corner.'},
    'closet':{'name':'Closet','north':'bedroom', 'east': 'hidden',
    'text':'There are some old robes hanging on a rusted metal rod. An old shattered mirror sits on your left and the mirror pieces are placed neaty in a line on the floor.'},
    'hidden':{'name':'Secret Room','west':'closet','text':'You enter a hidden door behind the clothes. There is a metal rack and iron maiden on your left, and some dark stains on the floor.'},
    'guest':{'name':'Guest Room','east': 'dining','text': 'There is a fancy bed in the middle of the room. Guests probably stayed here.'}}
directions = ['north', 'south', 'east', 'west']
current_room = rooms['entrance']

#treasure is in a random room
right_list = list(rooms.keys())
right_list.remove('entrance')
chosen_room = random.choice(right_list)
right_room = rooms[chosen_room]
gottreasure = False

#game loop
while True:
    #show room name when you enter
    print()
    print('You are in the {}.'.format(current_room['name']))
    print(current_room['text'])

#to make it possible to win
    if gottreasure is True and current_room == rooms['entrance']:
        print('You did it! You got the treasure and escaped in time!')
        end()
        quit()

    elif gottreasure is False and current_room == right_room:
        print('Next to the old wooden cabinet you see a box full of treasure. You pick up the box, and stuff it in your backpack. \n Now all you have to do is to get out of this creepy house.')
        gottreasure = True
    elif gottreasure is True and not current_room == rooms['entrance']:
        print('Get to the Entry Way before its too late!')

#to not have the whole display every Time
    while True:
        #user input
        userinput = input('What do you want to go?\n').strip()
        dir = userinput.lower()
        #movement
        if dir in directions:
            if dir in current_room:
                current_room = rooms[current_room[dir]]
                break
            else:
                print('You cannot go that way')
        elif dir == 'quit':
            end()
            quit()
        else:
            print('You can only go north/south/east/west. Where do you want to go?')
