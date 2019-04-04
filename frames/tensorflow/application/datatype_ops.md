
- constant
    - Constants are stored in the graph definition.
    - loading graphs expensive when constants are big
        - Only use constants for primitive types.
        - Use variables or readers for more data that requires more memory
    - tf.constant is an op
    - A constant's value is stored in the graph and replicated wherever the graph is loaded. A variable is stored separately, and may live on a parameter server.


- variable
    - tf.Variable is a class with many ops
    - You can feed values to tensors that aren't placeholders. 
        - a = tf.add(2, 5)  print(sess.run(b, feed_dict={a: 15})) 
    

- feedable tensor
    - 
    
- data
    - does tf.data really perform better?
        - speed
            - With placeholder: 9.05271519 seconds
            - With tf.data: 6.12285947 seconds
        - drawbacks
            - For prototyping, feed dict can be faster and easier to write (pythonic)
            - tf.data is tricky to use when you have complicated preprocessing or multiple data sources
            - NLP data is normally just a sequence of integers. In this case, transferring the data over to GPU is pretty quick, so the speedup of tf.data isn't that large
    

