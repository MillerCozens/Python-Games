import os
import time 

#####MENU#####       

def getmenuoptions():
    print()
    choice = None
    choice = input("""
    -----Menu-----
    Please Choose an Option
    A: Games
    B: Quit
    Created by: Miller Cozens, Ben Norman.

: """)

    if choice == 'A' or choice == 'a':
        time.sleep(0.2)
        Games()
    elif choice == 'B' or choice == 'b':
        quit()
    else:
        print("You did not select an option, please select an option to continue")
        getmenuoptions()

def Games():
    print()

    choice = input("""
    ----------
    1: Pong
    2: Snake
    3: Textris
    4: Space Invaders
    5: Hang Man
    6: Main Menu
: """)

    if choice == '1':
        os.system("Pong.py")
    elif choice == '2':
        os.system("Snake.py")
        return
    elif choice == '3':
        return
    elif choice == '4':
        os.system("spaceinvaders.py")
        return
    elif choice == '5':
        return
    elif choice == '6':
        time.sleep(0.2)
        getmenuoptions()
    else:
        print("You did not select a stage, please select a stage to continue")
    Games()

getmenuoptions()




    
