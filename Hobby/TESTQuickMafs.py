# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:47:01 2019

@author: sherv
"""
import numpy as np
import time


def gennumber(n1=100,n2=100, dec1=True, dec2=True):
    '''
    generate two random floats between 0 and n1.dec1 and n2.dec2 respectively. 
    if dec_i=False it will return two integers.
    '''
    a = np.random.randint(2,n1)
    b = np.random.randint(2,n2)
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


def timed(A,B, op):
    '''
    check the operation and print the question. Get response of user and time it. 
    returns answer and elapsed time in a tuple. 
    '''
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
    '''
    checks input against the correct answer and responds; in case of wrong answer
    correct answer is also printed. Also returns a string to show whether answer is 
    correct (c), blank (b) or wrong (w).
    '''
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


def choices(A,B):
    ABC = ["A", "B", "C"]
    view = {}
    for j in range(len(ABC)-1):
        plusminus = np.random.choice([True,False])
        if plusminus == True:
            plus = round((1+np.random.random())+(A*B),3)
            while plus == round((A*B),3):
                plus = round((1+np.random.random())+(A*B),3)
            view[np.random.choice(ABC)] = plus
        else:
            minus = round((1-np.random.random())+(A*B),3)
            while minus == round(A*B,3):
                minus = round((1-np.random.random())+(A*B),3)
            view[np.random.choice(ABC)] = minus
    for abc in ABC:
        if abc in ABC and abc not in view.keys():
            view[abc] = round((A*B),3)
        else: pass
    for abc in sorted(list(view.keys())):
        print(f"{abc}.", view[abc])
        
        
#def timeout(signal,frame):
#    raise Exception("time's up!")

operations = ["+", "-", "*", "/", "*", "*"]
quitresponse = ["yes", "y", "t", "true", "+", "q", "quit"]


while True:
    Quit = input("Quit? ").lower()
    if Quit not in quitresponse: 
        T = 0
        question = 0
        grade = 0
        limit = 600
        T_end = time.monotonic() + limit
        try:           
            while time.monotonic()<T_end and question<75: # use signal instead and remove the time check after the for loops
                print("\n","stage 1")
                for i in range(30):
                    if time.monotonic()<T_end:
                        question += 1
                        op = np.random.choice(operations)
                        A,B= gennumber(n1=12,dec1=False, dec2 = False)
                        ans, Elapsed = timed(A, B, op) 
                        points = check(A,B, op, ans)
                        if points == "c":
                            grade += 1
                        elif points == "b":
                            grade -= 2
                        elif points =="w":
                            grade -= 3 
                        T+= Elapsed
                        print("Total time (seconds):", T)
                    else: break
            
                print("\n","stage 2")
                for i in range(15):
                    if time.monotonic()<T_end:
                        question += 1
                        op = np.random.choice(operations)
                        A,B= gennumber(n1=12, n2=12, dec2=False)
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
                    else: break
                for i in range(15):
                    if time.monotonic()<T_end:
                        question += 1
                        op = np.random.choice(operations)
                        A,B= gennumber(n1=12, dec2=False)
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
                    else: break
             
                print("\n","stage 3")
                for i in range(15):
                    if time.monotonic()<T_end:
                        question += 1
                        op = "*"
                        A,B= gennumber(n1=1000)
                        choices(A,B)
                        ans, Elapsed = timed(A, B, op) 
                        points = check(A,B, op, ans)
                        if points == "c":
                            grade += 2
                        elif points == "b":
                            grade -= 1
                        elif points =="w":
                            grade -= 2
                        T+= Elapsed
                        print("Total time (seconds):", T)
                    else: break
                    
        except:
            print("\n")  
            print("Total time (seconds): ", T)
            print("Questions:", question)
            print("Points: ", grade)
        
    else:
        print("Total time (seconds): ", T)
        print("Questions:", question)
        print("Points: ", grade)
        break
    
