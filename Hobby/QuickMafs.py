# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 13:05:28 2018

@author: sherv
"""

import numpy as np 

print('Wlecome to the \'quick mafs\' practice game' )

 # The game:
while True:
    print('If you wish to quit, please enter: \' quit \'')
    print('For help, please enter: \' help \'')
    math = input('Please choose from: +, -, *, / \n')
    if math == '-':
        a = np.random.randint(0,999)
        b = np.random.randint(0,999) 
       # Only generate numbers that will give positive results
        while b > a:    
            b = np.random.randint(0,999)
            if b < a:
                pass
            else: 
                b = np.random.randint(0,999)
        
        ans = input('%f - %f =' %(a, b))
        if ans == str(a-b):
            print('Correct')
        else:
            print('Wrong')
            print(a-b)
    elif math == '+':
        a = np.random.randint(0,999)
        b = np.random.randint(0,999)
        ans = input('%f + %f =' %(a, b))
        if ans == str(a+b):
            print('Correct')
        else:
            print('Wrong')
            print(a+b)
    elif math == '*':
        a = round(np.random.randint(0,100))
        b = round(np.random.randint(0,100))
        ans = input('%f * %f =' %(a, b))
        if ans == str(a*b):
            print('Correct')
        else:
            print('Wrong')
            print(a*b)
    elif math == '/':
        a = round(np.random.randint(2,100))
        b = round(np.random.randint(2,100))
        
        while b > a:    
            b = np.random.randint(2,100)
            if b < a:
                pass
            else: 
                b = np.random.randint(2,100)
        
        ans = input('%f / %f =' %(a, b))
        if ans == str(a/b):
            print('Correct')
        else:
            print('Wrong')
            print(a/b)
    elif math == 'quit':
        break
    elif math == 'help':
        print('The aim of the game is for you to practice your mental maths skills.',
              'You can choose one of the four main operations to practice.',
              'Two random numbers will be generated and you will need to enter your answer.')
    else:
        continue
print('Thanks for playing')