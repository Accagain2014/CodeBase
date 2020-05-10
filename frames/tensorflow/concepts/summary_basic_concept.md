- tensorflow
    - tensor + flow = data + flow

- tensor
    - An n-dimensional array
    - data
    
- Nodes
    - operators, variables, and constants

- Edges
    - tensors

- Session
    - A Session object encapsulates the environment in which Operation objects are executed, and Tensor objects are evaluated.
    - Session.run(), which hands the graph off for execution to the C++ runtime.
    - Session will also allocate memory to store the current values of variables.
    - Session looks at all trainable variables that loss depends on and update them.
    
- Graph
    - why need Graph?
        - Save computation. Only run subgraphs that lead to the values you want to fetch.
        - Break computation into small, differential pieces to facilitate auto-differentiation
        - Facilitate distributed computation, spread the work across multiple CPUs, GPUs, TPUs, or other devices
    - Pros
        - Optimizable
            - automatic buffer reuse
            - constant folding
            - inter-op parallelism
            - automatic trade-off between compute and memory
        - Deployable
            - the Graph is an intermediate representation for models
        - Rewritable
            - experiment with automatic device placement or quantization
    - Cons
        - Difficult to debug
            - errors are reported long after graph construction
            - execution cannot be debugged with pdb or print statements
        - Un-Pythonic
            - writing a TensorFlow program is an exercise in metaprogramming
            - control flow (e.g., tf.while_loop) differs from Python [for 是否可行？]
            - can't easily mix graph construction with custom data structures

- ops
    - constants
    - variables
    - operators
    

- get the value of a node
    - Create a session, assign it to variable sess so we can call it later
    - Within the session, evaluate the graph to fetch the value of a
    
    
- lazy loading
    - 先确定op, 建图，然后再执行，而不是每次执行时，增加op.
    - refers to a programming pattern when you defer declaring/initializing an object until it is loaded.
    - In the context of TensorFlow, it means you defer creating an op until you need to compute it.
    - separate the definition of ops and their execution
    - ![](../../../images/tf/laza_load.jpg)
    - ![](../../../images/tf/norm_load.jpg)
    - 解决方案实现:
        - Use Python attribute to ensure a function is only loaded the first time it’s called
    
- eager execution
    - PyTorch's dynamic graphs
    - "A NumPy-like library for numerical computation with support for GPU acceleration and automatic differentiation, and a flexible platform for machine learning research and experimentation."
    - Eager execution: Execute compositions with Python 
    - Graph construction: Execute compositions of operations with Sessions
 

- scope
    - name scope
        - Group nodes together with tf.name_scope(name)
        - 作用于操作
        
    - variable scope
        - Variable scope facilitates variable sharing
        - get_variable
            - If a variable with <name> already exists, reuse it, If not, initialize it with <shape> using <initializer>
            - scope.reuse_variables()
    - the two relations
        - tf.variable_scope implicitly creates a name scope
            
- tf.train.Saver
    - Only save variables, not graph
    - Checkpoints map variable names to tensors
    - Still need to build your graph

- tf.summary
    - tf.summary.scalar
    - tf.summary.histogram
    - tf.summary.image
    
 
- not just a library
    - TensorFlow
    - TensorBoard
    - Tensor Serving


- with other frames
    - Numpy
        - NumPy supports ndarray, but doesn't offer methods to create tensor functions and automatically compute derivatives, nor GPU support.
        - TensorFlow can be more efficient than NumPy because TensorFlow knows the entire computation graph that must be executed, while NumPy only knows the computation of a single mathematical operation at a time.
        - TensorFlow can also automatically calculate the gradients that are needed to optimize the variables of the graph so as to make the model perform better.
         
        
    - PyTorch
        - PyTorch’s dynamic graphs.
        