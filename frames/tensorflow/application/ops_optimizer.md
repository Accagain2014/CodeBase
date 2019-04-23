## tips
    - “Advanced” optimizers work better when tuned, but are generally harder to tune

## examples
    - optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)
        - Session looks at all trainable variables that loss depends on and update them
        
## categories
    - tf.train.GradientDescentOptimizer

    - tf.train.AdagradOptimizer
    - tf.train.MomentumOptimizer
    - tf.train.AdamOptimizer
    - tf.train.FtrlOptimizer
    - tf.train.RMSPropOptimizer
