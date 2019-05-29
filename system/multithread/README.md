
## Useful Links
- [Parallel Processes in Python, course](http://selkie.macalester.edu/csinparallel/modules/ParallelProcessesInPython/build/html/index.html)
- [Parallel Processing in Python – A Practical Guide with Examples](https://www.machinelearningplus.com/python/parallel-processing-python/)



## problems
- How to structure the code and understand the syntax to enable parallel processing using multiprocessing?
- How to implement synchronous and asynchronous parallel processing?
- How to parallelize a Pandas DataFrame?
- 



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
        
