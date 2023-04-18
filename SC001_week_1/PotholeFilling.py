"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:
    post-condition:
    """
    for i in range(3):
        go_in()
        put_99()
        go_out()


def put_99():
    for i in range(99):
        put_beeper()


def go_in():
    """
    pre-condition:Karel is at upper-left of the pothole,facing East.
    post-condition:Karel is in the pothole,facing South.
    """
    move()
    turn_right()
    move()


def go_out():
    """
    pre-condition:Karel is at upper-left of the pothole,facing East.
    post-condition:Karel is in the pothole,facing South.
    """
    turn_around()
    move()
    turn_right()
    move()


def turn_right():
    """
    pre-condition:
    post-condition:
    """
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()
















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
