import time
import QuickMafs

# from threading import Thread 
import multiprocessing
from threading import Thread 




if __name__ == "__main__":
    question = 0
    score = 0
    
    def timelimit():
        time.sleep(10)
        if correct != None:
            return
        print("too slow")

     
    
    while True: 
        # Main Menu
        print("If you wish to quit, please enter: 'quit'")
        print("For the score, please enter: 'score'")
        
        
        print("For help, please enter: 'help'")
        math = input('Please choose from: +, -, *, / \n')
        
        if math == 'quit':
            break
        
        elif math == 'help':
            print('The aim of the game is for you to practice your mental maths skills.',
                'You can choose one of the four main operations to practice.',
                'Two random numbers will be generated and you will need to enter your answer.')
            
        elif math == "score":
            try:
                print(f"Score: {score}/{question} ({round(score/question*100,2)}%)")
            except ZeroDivisionError:
                print("Score: 0/0 (0.0%)")

        elif math in ["+","*","-","/"]:
            question += 1
            ez = input("choose difficulty: Easy (True), or hard (False)? ").lower()
            if ez == "quit":
                break
            
            elif ["He chose hard" for t in list(ez) if t == "f"]:
                ez = False
            else:
                ez = True

            correct = None
            Thread(target = timelimit).start()
            correct = QuickMafs.play(math, ez)   
            if correct:
                score += 1
            
            
            
        else:
            continue
        
    print('Thanks for playing')
