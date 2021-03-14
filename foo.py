#!/usr/bin/env python

from random import randint

def one_d_six():
    return randint(1,6)

def three_d_six():
    return one_d_six() * one_d_six() * one_d_six()

def roll_character():
    return {
        'strength': three_d_six(),
        'intelligence' : three_d_six()
    }
