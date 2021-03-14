#!/usr/bin/env python3

from random import *

def d6():
    return randint(1,6)

def rollcharacter(name, char_class):
    character = {'name': name, 'char_class': char_class}
    character['str'] = d6() + d6() + d6()
    return character

c=rollcharacter('Jim', 'Mage')

print(c)
