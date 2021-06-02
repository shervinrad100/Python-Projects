import time
import QuickMafs
import concurrent.futures
from threading import Timer
import msvcrt


class TimeoutExpired(Exception):
    pass

def tooslow(timer):
    global break_thread
    end = time.time() + timer
    while not break_thread and time.time() < end:
        time.sleep(1)
    if time.time() > end:
        print("too slow")

def tooslow2(timer):
    global ans
    end = time.time() + timer
    while ans is None and time.time() < end:
        time.sleep(1)
    if time.time() > end:
        print("too slow")

def input_with_timeout(a,b,timer):
    end = time.time() + timer
    print('%.2f - %.2f =' %(a, b))
    result = []
    while time.time() < end:
        if msvcrt.kbhit():
            result.append(msvcrt.getwche())
            if result[-1] == "\r":
                return "".join(result[:-1])
    raise TimeoutExpired

if __name__ == "__main__":
    question = 0
    score = 0
    timer = 5

    while True: 
        # Main Menu
        print("If you wish to quit, please enter: 'quit'")
        print("For the score, please enter: 'score'")
        print("For help, please enter: 'help'")

        math = input('\nPlease choose from: +, -, *, / \n').strip()
        
        if math == 'quit':
            break
        
        elif math == 'help':
            print('The aim of the game is for you to practice your mental maths skills.',
                'You can choose one of the four main operations to practice.',
                'Two random numbers will be generated and you will need to enter your answer.')
            print('To quit type "quit", to edit timer type "timer", to see score type "score"')
            
        elif math == "score":
            try:
                print(f"\nScore: {score}/{question} ({round(score/question*100,2)}%)\n")
            except ZeroDivisionError:
                print("Score: 0/0 (0.0%)")
        
        elif math == "timer":
            timer = int(input("Enter timer length as an integer: ").strip())
            print(f"timer set for {timer} seconds")

        elif math in ["+","*","-","/"]:
            
            ez = input("choose difficulty: Easy (True), or hard (False)? ").strip().lower()
            
            if ez == "quit":
                break
            
            elif ["He chose hard" for t in list(ez) if t == "f"]:
                ez = False
            else:
                ez = True
            
            
            question += 1
            """
            # method 1
            stopwatch = Timer(timer, print, ["too slow"])
            stopwatch.start()
            ans = QuickMafs.play(math, ez)
            stopwatch.cancel()
            """

            # method 2
            ans = None
            with concurrent.futures.ThreadPoolExecutor() as executor:
                stopwatch = executor.submit(tooslow2, timer)
                ans = QuickMafs.play(math, ez)

            """
            # method 3
            break_thread = False
            with concurrent.futures.ThreadPoolExecutor() as executor:
                stopwatch = executor.submit(tooslow, timer)
                ans = QuickMafs.play(math, ez)
                break_thread = True
            
            # method 4
            
            change play function to have a timed input function instead of the standard input

            try:
                ans = input_with_timeout(timer)
            except TimeoutExpired:
                print("too slow")

            """

            if ans is True:
                score += 1


        else:
            continue
        
    print('Thanks for playing')
