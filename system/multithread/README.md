
## Useful Links
- [Parallel Processes in Python, course](http://selkie.macalester.edu/csinparallel/modules/ParallelProcessesInPython/build/html/index.html)
- [Parallel Processing in Python – A Practical Guide with Examples](https://www.machinelearningplus.com/python/parallel-processing-python/)



## problems
- How to structure the code and understand the syntax to enable parallel processing using multiprocessing?
- How to implement synchronous and asynchronous parallel processing?



## concepts
- Synchronous execution
    - A synchronous execution is one the processes are completed in the same order in which it was started. 
    - This is achieved by locking the main program until the respective processes are finished.
    - Pool.map() and Pool.starmap()
        - map can take only one iterable as an argument.
        - map() is really more suitable for simpler iterable operations but does the job faster.
    - Pool.apply()
        - takes an args argument that accepts the parameters passed to the ‘function-to-be-parallelized’ as an argument,
    
    
- Asynchronous execution
    - doesn’t involve locking.
    - Pool.map_async() and Pool.starmap_async(), Pool.apply_async()
    

## module
- multiprocessing
    - is used to run independent parallel processes by using **subprocesses** (instead of threads).
    - the processes can be run in completely separate memory locations.
    - Main class
        - Pool
        - Process
- os.system("cmd")
- subprocess.run(["df", "-h", "/home"])
- **pathos** 对自定义class不能序列化的，可以采用 [pathos](https://github.com/uqfoundation/pathos)
    - dill: a utility to serialize all of python
    - This is because dill is used instead of pickle or cPickle, and dill can serialize almost anything in python.
    - https://stackoverflow.com/questions/1816958/cant-pickle-type-instancemethod-when-using-multiprocessing-pool-map
    
    