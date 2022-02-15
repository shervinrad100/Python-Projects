# Goal
    To set a timer so that if you dont input your answer within a specific time, 
    the input() method would stop and the object would be set to None. 

# Ideas
    I had two ideas on setting a timer on the question
        1. multiprocessing
            timer runs on one process and input() runs on another, 
            the first process that finishes, writes to the ans object.
            From there, there is a check in the other thread:
            if object is None, kill the process else join to main process
        2. threading 
            you create a thread that starts a timer and prints "too slow"
            in the mean time, the main thread is waiting for you to input 
            your answer. 
            
# Problems 
    - The problem with multiprocessing is that the Global Interpreter Lock (GIL) 
    doesnt allow I/O when parallel processing. Also, because each process has an 
    independent GIL, the processes cant write to a shared object. 

    - I tried having a timeout exception raised if the input() thread is not completed
    in t < timer. The issue is that the exception is only raised after input has been 
    entered. 


# multiprocessing VS threading

    - a new thread is spawned within the existing process
    - startign a thread is faster than starting a process
    - memory is shared between all threads but processes have independent memory 
    allocation
    - one GIL for all threads whereas multiprocessing has a GIL for each process
    - mutexes necessary to control access to shared data
        MUTEX is an object that is shared but only held by one entity at any point
    - Threading is used for I/O bound processes whereas multiprocessing is for 
    CPU bound processes


# concurrent.futures 

## executor
    ### executor.submit()
        creates ONE futures object (thread or a process), passing into it *args **kwargs
            
            - to access the results you must use the .result() method on the futures object
            - the object is executed immediately as its created 

            eg: 
            executor.submit(func, args)

    ### executor.map() 
        creates an iterable with len(iterable) objects. These are the results of the 
        threads for each item in the iterable that is mapped to your function
            
            - the results are stored in the iterable readily

            eg: 
            executor.map(func, args_iterable)

## as_completed()
    for all the futures it receives in it iterable, it sets up a callback to fire when 
    the future is done. Once the callback is received, as_completed yields the result 
    of the future. In essence, it yields the results of threads in order that they are 
    completed.

        eg:
         futures = [executor.submit(func, args) for args in args_iterable]
         print([future.result() for future in concurrent.futures.as_completed(futures)])
    
## futures.join()
    ensures the thread is completed and is joined into the main thread.
    
    

    
