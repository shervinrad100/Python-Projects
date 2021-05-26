# exercise to improve arithmetic maths 


import numpy as np 
import time

print('Welcome to the \'quick mafs\' practice game' ) # implement negative marks 
question = 0
score = 0

def gennumber(a_large=False, start=2):
    """
    generates four numbers:
    - two random integers between 2 and 100 with option to choose a > b and the min of range
    - two decimals with 0.01 precision between 0 and 1
    """
    a = np.random.randint(start,999)
    b = np.random.randint(start,999)
    a2 = round(np.random.random(),2)
    b2 = round(np.random.random(),2)
    if a_large:
        while b < a:
            b = np.random.randint(2,999)
    return a,b,a2,b2



 # The game:
def play():
    while True:
        # Main Menu
        print('If you wish to quit, please enter: \' quit \'')
        ez = input("choose difficulty: Easy (True), or hard (False)? ").lower()
        
        if ez == "quit":
            break
        elif ["ez" for t in list(ez) if t == "t"]:
            ez = True
        else:
            ez = False
        
        print('For help, please enter: \' help \'')
        math = input('Please choose from: +, -, *, / \n')

    # Subtraction
        if math == '-':
            a,b,a2,b2 = gennumber(True)
            question += 1 
        # Only generate numbers that will give positive results
            if not ez:
                a += a2
                b += b2
            
            startT = time.time()
            ans = input('%.2f - %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a-b,2)):
                print('Correct')
                score += 1
            else:
                print('Wrong')
                print(round(a-b,2))
            

    # Summation    
        elif math == '+':
            a,b,a2,b2 = gennumber(False, 0)
            question += 1
            if not ez:
                a += a2
                b += b2
            
            startT = time.time()
            ans = input('%.2f + %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a+b,2)):
                print('Correct')
                score += 1
            else:
                print('Wrong')
                print(round(a+b,2))
            

    # Multiplication      
        elif math == '*':
            a,b,a2,b2 = gennumber(False)
            question += 1
            if not ez:
                a += a2
                b += b2

            startT = time.time()
            ans = input('%.2f * %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a*b,2)):
                print('Correct')
                score += 1
            else:
                print('Wrong')
                print(round(a*b,2))
            

    # Division
        elif math == '/':
            a,b,a2,b2 = gennumber(True)
            question += 1
            if not ez:
                a += a2
                b += b2
        
            startT = time.time()
            ans = input('%.2f / %.2f =' %(a, b))
            endT = time.time()
            print(f"Time elapsed: {int(endT-startT)}s")
            if ans == str(round(a/b),2):
                print('Correct')
                score += 1
            else:
                print('Wrong')
                print("%.2f" %(round(a/b,2)))
            
        elif math == 'quit':
            break
        
        elif math == 'help':
            print('The aim of the game is for you to practice your mental maths skills.',
                'You can choose one of the four main operations to practice.',
                'Two random numbers will be generated and you will need to enter your answer.')
            
        else:
            continue
        
    print('Thanks for playing')
if __name__ == "__main__":
    play()