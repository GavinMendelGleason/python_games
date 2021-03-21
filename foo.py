#!/usr/bin/env python

from random import randint
from re import match

CHAR_STATS = {
    'mage' : {
        'str' : -1,
        'int' : 1,
        'con' : 0,
        'agi' : 0,
        'app' : 1
    },
    'fighter' : {
        'str' : 1,
        'int' : -1,
        'con' : 1,
        'agi' : 0,
        'app' : 0
    },
    'rogue' : {
         'str' : 0,
         'int' : 1,
         'con' : -1,
         'agi' : 1,
         'app' : 0
    }
}

def one_d_six():
    return randint(1,6)

def three_d_six():
    return one_d_six() + one_d_six() + one_d_six()

def roll_character():
    return {
        'strength': three_d_six(),
        'intelligence' : three_d_six()
    }

def char_stats(stat,char_class):
    return CHAR_STATS[char_class][stat]

def class_name(class_number):
    if class_number=="1":
        return "mage"
    elif class_number=="2":
        return "fighter"
    elif class_number=="3":
        return "rogue"
    else:
        raise ValueError("Unknown class number")

def main():
    print("Hello, you are playing ULTIMATE SUPER ARENA DEATH MATCH")
    print("What is the name of your character?:")
    name=input()
    cls=None
    while cls==None:
        print("What is your class? Choose a number:")
        print("1. Mage 2. Fighter 3. Rogue")
        cls=input()
        if cls in ["1","2","3"]:
            pass
        else:
            cls=None
            print("That is not a valid character class!")
    print(f"Welcome, {name}")
    cls_name=class_name(cls)
    print(f"Welcome to the guild of {cls_name}s")
    if cls_name=="mage":
        spell=None
        while spell==None:
            print("What spells would you like? (Choose 2 numbers seperated by commas)")
            print("1. Fireball 2. Freeze 3. Heal 4. Bless 5. Hide")
            spell=input()
            r = match("(\d)+(,|\s)(\d)+", spell)
            spell1=r[1]
            spell2=r[3]
            validspells=["1","2","3","4","5"]
            if spell1 in validspells and spell2 in validspells:
                pass
            else:
                spell=None
                print("That is not a valid spell, please pick two valiid spells")
