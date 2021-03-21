#!/usr/bin/env python3

from random import randint
from re import match

CHAR_STATS = {
    'mage' : {
        'str' : -1,
        'int' : 1,
        'con' : 0,
        'agi' : 0,
        'cha' : 1
    },
    'fighter' : {
        'str' : 1,
        'int' : -1,
        'con' : 1,
        'agi' : 0,
        'cha' : 0
    },
    'rogue' : {
        'str' : 1,
        'int' : 0,
        'con' : -1,
        'agi' : 1,
        'cha' : 0
    }
}

def d6():
    return randint(1,6)

def rollcharacter(name, char_class):
    character = {'name': name, 'char_class': char_class}
    character['str'] = d6() + d6() + d6() + CHAR_STATS[char_class]['str']
    character['int'] = d6() + d6() + d6() + CHAR_STATS[char_class]['int']
    character['con'] = d6() + d6() + d6() + CHAR_STATS[char_class]['con']
    character['agi'] = d6() + d6() + d6() + CHAR_STATS[char_class]['agi']
    character['cha'] = d6() + d6() + d6() + CHAR_STATS[char_class]['cha']

    return character

def printcharacter(character):
    print(f"Name : {character['name']}")
    print(f"Character class : {character['char_class']}")
    print(f"Str : {character['str']}")
    print(f"Int : {character['int']}")
    print(f"Con : {character['con']}")
    print(f"Agi : {character['agi']}")
    print(f"Cha : {character['cha']}")

def selectcharacter():
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
    cls_name=class_name(cls)
    return [name, cls_name]

def class_name(class_number):
    if class_number=="1":
        return "mage"
    elif class_number=="2":
        return "fighter"
    elif class_number=="3":
        return "rogue"
    else:
        raise ValueError("Unknown class number")

def selectspells(cls_name):
    if cls_name=="mage", "rogue":
    spell_number=None
    if cls_name=="mage"
        while spell_number==None:
            print("What spells would you like? (Choose 2 numbers seperated by commas)")
            print("1. Fireball 2. Freeze 3. Heal 4. Bless 5. Hide")
            spell_number=input()
            r = match("(\d)+(,|\s)(\d)+", spell)
            spell1=r[1]
            spell2=r[3]
            validspells=["1","2","3","4","5"]
            if spell1 in validspells and spell2 in validspells:
                pass
            else:
                spell_number=None
                print("That is not a valid spell, please pick two valid spells")
    if cls_name=="rogue"
        while spell_number==None:
            print("What spells would you like? (Choose 1 number)")
            print("1. Hide 2. Cloak 3. Identify")
            spell_number=input()
            validspells=["1","2","3"]
            if spell_number in validspells:
                pass
            else:
                spell_number=None
                print("That is not a valid spell, please pick one valid spell")

def spell_name(spell_number):
    if cls_name=="mage"
        if spell_number=="1":
            return "Fireball"
        elif spell_number=="2":
            return "Freeze"
        elif spell_number=="3":
            return "Heal"
        elif spell_number=="4":
            return "Bless"
        elif spell_number=="5":
            return "Hide"
        else:
            raise ValueError("Unknown spell number!")
    if cls_name=="rogue"
        if spell_number=="1":
            return "Hide"
        elif spell_number=="2":
            return "Cloak"
        elif spell_number=="3":
            return "Identify"
        else:
            raise ValueError("Unknown spell number!")

def selectroll(name, char_class):
    keep=None
    while keep==None:
        c=rollcharacter(name, char_class)
        printcharacter(c)
        print("Are these your final stats? Y/N")
        keep=input()
        if keep in ['y', 'Y', 'yes', 'Yes']:
            pass
        else:
            keep=None
    return c

def main():
    print("Hello, you are playing ULTIMATE SUPER ARENA DEATH MATCH")
    [name, cls_name]=selectcharacter()
    print(f"Welcome, {name}")
    print(f"Welcome to the guild of {cls_name}s")
    c=selectroll(name, cls_name)
