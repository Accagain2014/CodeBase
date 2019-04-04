
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
    

