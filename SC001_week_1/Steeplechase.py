"""
File: Steeplechase.py
Name: wenyi
---------------------------------
Pre-condition:
Post-condition:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    """
    pre-conditon:Karel is at the left side of the wall,facing east
    post-conditon:Karel is at the right side of the wall
    """
    up()
    cross()
    down()
    turn_left()


def down():
    while front_is_clear():
        move()


def cross():
    """
    pre-conditon:Karel is facing North,at the upper left
    post-conditon:
    """
    move()
    turn_right()


def up():
    """
        pre-conditon:Karel is at the right side of the wall
        post-conditon:
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()
    # turn_left()
    # # Karel is facing North
    # while not right_is_clear():
    #     move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()




















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
