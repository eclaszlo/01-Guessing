import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit = False
range = 100

while not quit:
    random_number = random.randint(1,range)
    count =  1
    number = -1
    while number  != random_number:
        number = input("\nI'm thinking of a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("\nThink you're being funny, eh? Try picking a *number* this time.")
        else:    
            number = int(number)
            count = count + 1
            print("Nope, sorry.")  
            if number > random_number:
                print("Too high")
            elif number < random_number:
                print("Too low")          
    print("You finally got it right!")
    print("It only took you {} tries".format(count))
    try_again = input("\nWould you like to try again for a better score (yes or...yes)?")
    try_again = try_again.lower()
    if try_again == "yes" or try_again == "y" :
        print("Okay. Maybe try a little harder this time, yeah?")
        quit = False
    else: 
        print("I see how it is. Your loss then.")
        quit = True


        print("\n\nSee you next time!")