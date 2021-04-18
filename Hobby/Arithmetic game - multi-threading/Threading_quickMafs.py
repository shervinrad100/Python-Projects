import time
import msvcrt
import sys

"""
def diff(difficulty):
    if difficulty like "hard":
        t = 3
    elif difficulty like "medium":
        t = 5
    else:
        t = 3
"""


class TimeoutExpired(Exception):
    pass

def input_with_timeout(prompt, timeout):
    timer = time.monotonic
    sys.stdout.write(prompt)
    sys.stdout.flush() 
    endtime = timer() + timeout
    result = []
    while timer() < endtime:
        if msvcrt.kbhit():    
            result.append(msvcrt.getwche())
            if result[-1] == "\n" or result == " ":
                return ''.join(result[:-1])
        time.sleep(0.04)
    raise TimeoutExpired
    
try:
    ans = input_with_timeout("2+2: \n",10)
    print(ans)
except TimeoutExpired:
    print("Time's Up")
else:
    print(ans)
