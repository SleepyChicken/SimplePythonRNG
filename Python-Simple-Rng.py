'''
        Written by SleepyChicken
'''

import random

i = 0                                                   # ----- Loop counter

x = 0                                                   # ----- For switch between a and b

randomNumber = []                                       # ----- Random number empty list 

a = int(input('From : '))                               # ----- Input number section 

b = int(input('To : '))

if b < a :                                              # ----- Switched number if first input is higher
    x = a
    a = b
    b = x

nRand = int(input('How many time ? : '))                # ----- How many time to random 

while i < nRand :                                       # ----- Random number 
    z = random.randrange(a, b)
    randomNumber.append(z)
    i = i + 1

print(randomNumber)