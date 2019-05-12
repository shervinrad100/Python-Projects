# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:47:01 2019

@author: sherv
"""
import numpy as np
import time


def gennumber(n1=100,n2=100, dec1=True, dec2=True):
    a = np.random.randint(0,n1)
    b = np.random.randint(0,n2)
    a2 = round(np.random.random(),2)
    b2 = round(np.random.random(),2)
    if dec1 == True:
        A = a+a2
    else:
        A = a
    if dec2 == True:
        B = b+b2
    else:
        B = b
    return A,B


def timed(A,B, op="*"):
    startT = time.time()
    if op == "/":
        if A>B:
            ans = input('%.2f / %.2f =' %(A, B))
        else:
            ans = input('%.2f / %.2f =' %(B, A))
    elif op == "+":
        ans = input('%.2f + %.2f =' %(A, B))
    elif op == "-":
        if A>B:
            ans = input('%.2f - %.2f =' %(A, B))
        else:
            ans = input('%.2f - %.2f =' %(B, A))    
    else:
        ans = input('%.2f * %.2f =' %(A, B))
    endT = time.time()
    elapsed = int(endT-startT)
#    print(f"Time elapsed: {elapsed}s")
    return ans, elapsed
    

def check(A,B, op, ans):
    if op == "*":
        if ans == str(round((A)*(B),2)):
            print('Correct')
            point = "c"
        elif ans == "":
            point = "b"
        else:
            print('Wrong')
            print(round((A)*(B),2))
            point = "w"
    if op == "+":
        if ans == str(round(A+B,2)):
            print("Correct")
            point="c"
        elif ans == "":
            point = "b"
        else:
            print("Wrong")
            print(round(A+B,2))
            point = "w"
    if op == "/":
        if A>B:
            if ans == str(round(A/B,2)):
                print("Correct")
                point = "c"
            elif ans == "":
                point = "b"
            else:
                print("Wrong")
                print(round(A/B,2))
                point = "w"
        else:
            if ans == str(round(B/A,2)):
                print("Correct")
                point = "c"
            elif ans == "":
                point="b"
            else:
                print("Wrong")
                print(round(B/A,2))
                point = "w"
    if op == "-":
        if A>B:
            if ans == str(round(A-B,2)):
                print("Correct")
                point = "c"
            elif ans == "":
                point = "b"
            else:
                print("Wrong")
                print(round(A-B,2))
                point = "w"
        else:
            if ans == str(round(B-A,2)):
                print("Correct")
                point = "c"
            elif ans =="":
                point = "b"
            else:
                print("Wrong")
                print(round(B-A,2))   
                point = "w"
    return point


operations = ["+", "-", "*", "/", "*", "*"]
response = ["yes", "y", "t", "true", "+", "q", "quit"]


while True:
    Quit = input("Quit? ").lower()
    if Quit not in response: 
        
        T = 0
        question = 0
        grade = 0
        try:
            limit = int(input("time limit (seconds): "))+1
        except:
            limit = 600
        
        while T<limit and question<75:
            # stage 1
            for i in range(30):
                question += 1
                op = np.random.choice(operations)
                A,B= gennumber(n1=12,dec1=False, dec2 = False)
                ans, Elapsed = timed(A, B, op) 
                points = check(A,B, op, ans)
                check(A,B,op, ans)
                if points == "c":
                    grade += 1
                elif points == "b":
                    grade -= 2
                elif points =="w":
                    grade -= 3 
                T+= Elapsed
                print("Total time (seconds):", T)
            
            # stage 2
            for i in range(30):
                question += 1
                op = np.random.choice(operations)
                A,B= gennumber()
                ans, Elapsed = timed(A, B, op) 
                points = check(A,B, op, ans)
                if points == "c":
                    grade += 2
                elif points == "b":
                    grade -= 1
                elif points =="w":
                    grade -= 1
                T+= Elapsed
                print("Total time (seconds):", T)
             
            # stage 3
            for i in range(15):
                question += 1
                op = "*"
                A,B= gennumber(n1=1000)
                ans, Elapsed = timed(A, B, op) 
                points = check(A,B, op, ans)
                check(A,B,op, ans)
                if points == "c":
                    grade += 2
                elif points == "b":
                    grade -= 1
                elif points =="w":
                    grade -= 2
                T+= Elapsed
                print("Total time (seconds):", T)
                
        print("\n")  
        print("Questions:", question)
        print("Points: ", grade)
        
    else:
        print("Total time (seconds): ", T)
        print("Questions:", question)
        print("Points: ", grade)
        break
    
