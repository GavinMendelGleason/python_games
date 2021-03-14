#!/usr/bin/env python

from random import randint

CHAR_STATS = {
    'mage' : {
        'str' : -1,
        'int' : 1,
        'con' : 0,
        'agi' : 0,
        'app' : 0
    },
    'fighter' : {
        'str' : 1,
        'int' : -1,
        'con' : 1,
        'agi' : 0,
        'app' : 1
    }
}

def one_d_six():
    return randint(1,6)

def three_d_six():
    return one_d_six() * one_d_six() * one_d_six()

def roll_character():
    return {
        'strength': three_d_six(),
        'intelligence' : three_d_six()
    }

def char_stats(stat,char_class):
    CHAR_STATS[char_class][stat]
