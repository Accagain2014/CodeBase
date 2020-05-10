
### two losses
- [Hvass-Labs/TensorFlow-Tutorials/12_Adversarial_Noise_MNIST.ipynb](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/12_Adversarial_Noise_MNIST.ipynb)
- created two optimizers for the neural network, one for the variables of the neural network and another for the single variable with the adversarial noise.
    - use collections to contain needed variables
        > 
            - ADVERSARY_VARIABLES = 'adversary_variables
            - collections = [tf.GraphKeys.GLOBAL_VARIABLES, ADVERSARY_VARIABLES]
            - x_noise = tf.Variable(tf.zeros([img_size, img_size, num_channels]),
                          name='x_noise', trainable=False,
                          collections=collections)
            - adversary_variables = tf.get_collection(ADVERSARY_VARIABLES)
            - optimizer = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(loss)
            - tf.train.AdamOptimizer(learning_rate=1e-2).minimize(loss_adversary, var_list=adversary_variables)
            
        > 
            - [var.name for var in tf.trainable_variables()]
            

### 正则化loss
- reg_losses = tf.get_collection(tf.GraphKeys.REGULARIZATION_LOSSES)  # 可以直接得到图上的权重的正则化loss