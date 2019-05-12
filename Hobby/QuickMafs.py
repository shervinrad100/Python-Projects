import numpy as np 
import time

print('Welcome to the \'quick mafs\' practice game' )
counter = 0
score = 0

def gennumber():
    a = np.random.randint(0,999)
    b = np.random.randint(0,999)
    a2 = round(np.random.random(),2)
    b2 = round(np.random.random(),2)
    while b > a:    
        b = np.random.randint(0,999)
    global counter                                                              # is this right?
    counter +=1    
    startT = time.time()
    ans = input('%.2f - %.2f =' %(a, b))
    endT = time.time()
    print(f"Time elapsed: {int(endT-startT)}s")
    return a,b,a2,b2, ans

 # The game:
while True:
    print('If you wish to quit, please enter: \' quit \'')
    print('For help, please enter: \' help \'')
    ez = input("Easy (True), or hard (False)? ").upper()
    EZ = ["TRUE" , "T" , "+"]
    if ez in EZ:
        ez = True
    elif ez == "quit":                                                          # not working?
        break
    else:
        ez = False
    math = input('Please choose from: +, -, *, / \n')

# Subtraction
    if math == '-':
        a = np.random.randint(0,999)
        b = np.random.randint(0,999)
        a2 = round(np.random.random(),2)
        b2 = round(np.random.random(),2)
       # Only generate numbers that will give positive results
        while b > a:    
            b = np.random.randint(0,999)
        if ez == True:
            startT = time.time()
            ans = input('%.2f - %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(a-b):
                print('Correct')
            else:
                print('Wrong')
                print(a-b)
        elif ez == False:
            startT = time.time()
            ans = input('%.2f - %.2f =' %(a+a2, b+b2))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a+a2-(b+b2),2)):
                print('Correct')
            else:
                print('Wrong')
                print(round(a+a2-(b+b2),2))

# Summation    
    elif math == '+':
        a = np.random.randint(0,999)
        b = np.random.randint(0,999)
        a2 = round(np.random.random(),2)
        b2 = round(np.random.random(),2)
        if ez == True:
            startT = time.time()
            ans = input('%.2f + %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(a+b):
                print('Correct')
            else:
                print('Wrong')
                print(a+b)
        elif ez == False:
            startT = time.time()
            ans = input('%.2f + %.2f =' %(a+a2, b+b2))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a+a2+b+b2,2)):
                print('Correct')
            else:
                print('Wrong')
                print(round((a+a2+b+b2),2))

# Multiplication      
    elif math == '*':
        a= np.random.randint(2,100)
        b= np.random.randint(2,100)
        a2 = round(np.random.random(),2)
        b2 = round(np.random.random(),2)
        if ez == True:
            startT = time.time()
            ans = input('%.2f * %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(a*b):
                print('Correct')
            else:
                print('Wrong')
                print(a*b)
        elif ez == False:
            startT = time.time()
            ans = input('%.2f * %.2f =' %(a+a2, b+b2))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str((a+a2)*(b+b2)):
                print('Correct')
            else:
                print('Wrong')
                print((a+a2)*(b+b2))

# Division
    elif math == '/':
        a= np.random.randint(2,100)
        b= np.random.randint(2,100)
        a2= round(np.random.random(),2)
        b2 = round(np.random.random(),2)
        while b > a:    
            b = np.random.randint(2,100)
        if ez == True:
            startT = time.time()
            ans = input('%.2f / %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round((a)/(b)),2):
                print('Correct')
            else:
                print('Wrong')
                print("%.2f" %((a)/(b)))
        elif ez == False:
            startT = time.time()
            ans = input('%.2f / %.2f =' %(a+a2, b+b2))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str((a+a2)/(b+b2)):
                print('Correct')
            else:
                print('Wrong')
                print("%.2f" %((a+a2)/(b+b2)))
        
    elif math == 'quit':
        break
    
    elif math == 'help':
        print('The aim of the game is for you to practice your mental maths skills.',
              'You can choose one of the four main operations to practice.',
              'Two random numbers will be generated and you will need to enter your answer.')
        
    else:
        continue
    
print('Thanks for playing')