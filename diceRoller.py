#Dice Roll program
#This simulates the rolling of a die.
roll = None
import random,time
#The above should be separated by a comma, no a semi-colon.
s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

def show_dice(roll):
    if roll == 1:
        print(s1)
    elif roll == 2:
        print(s2)
    elif roll == 3:
        print(s3)
    elif roll == 4:
        print(s4)
    elif roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)
    #All of the above ^^ needed to be elif statements, have TWO '+' signs, and a colon on the end, except the obvious differences in the last one.
    

def rollDice():
    print("rolling.....")
    global roll
    roll = random.randint(0,7)
    time.sleep(0.5)
    #roll = rand.randing(7) should be as above or the parameters are wrong and the random statement is spelled incorrectly, as is the int suffix.


while True:
    q1 = input("Type 1 to roll a die,\nType 2 to show the result,\nOr type 3 to do both together.")
    time.sleep(1)
    if q1 == 1:
        rollDice()
    elif q1 == 2:
        show_dice(roll)
    else:
        rollDice()
        time.sleep(1)
        show_dice(roll)

#There were unneeded indentations.

#There was a logic scope error, in that roll() kept the value for roll, so when show_dice() was called it did not have the variable so assigned 'None'.
#This was solved by making roll global.
