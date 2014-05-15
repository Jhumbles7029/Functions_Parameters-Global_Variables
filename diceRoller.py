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

def roll():
    print("rolling.....")
    roll = random.randint(0,7)
    global roll
#roll = rand.randing(7) should be as above or the parameters are wrong and the random statement is spelled incorrectly, as is the int suffix.

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

def rollDice():
    print("rolling.....")
    roll = random.randint(0,7)
    time.sleep(0.5)
    show_dice(roll)
#All of the above needed to be elif statements, have TWO '+' signs, and a colon on the end, except the obvious differences in the last one.

roll()
time.sleep(1)
show_dice(roll)
#These do not need indentations.


#There was a logic scope error in that roll() kept the value for roll, so when show_dice() was called it did not have the variable so assigned 'None'.
#This was solved by making roll global.
