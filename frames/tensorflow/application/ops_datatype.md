
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
    - Sessions allocate memory to store variable values
     


- three ways for data pipeline
    - Placeholder 
        - When you have a large graph and just want to test out certain parts, you can provide dummy values so TensorFlow won't waste time doing unnecessary computations.
        - 当图很大时，可以直接给后面变量赋值，直接测试要测试的部分
        - Placeholder variables serve as the input to the graph that we may change each time we execute the graph.
        - Pros
            - put the data processing outside TensorFlow, making it easy to do in Python
            - you get all the flexibility of Python, which makes it easy to work with arbitrary data formats.
        - Cons
            - users often end up processing their data in a single thread and creating data bottleneck that slows execution down. 
            - poor performance.
    
    - tf.data [Important link](https://docs.google.com/presentation/d/16kHNtQslt-yuJ3w8GIx-eEH6t_AvFeQOchqGRFpAD7U/edit#slide=id.g254d08e080_0_111)
        - Instead of doing inference with placeholders and feeding in data later, do inference directly with data.
        - Input pipelines = lazy lists. Functional programming to the rescue! 函数式编程, 组合高阶函数map/filter.
        - think of a Dataset as a lazy list of tuples of tensors. functional transformations.
        - a dataset can be a “source”, which means it’s created from one or more tensor objects...
        - important classes
            - tf.data.Dataset
                - from memroy
                    - tf.data.Dataset.from_tensor_slices((features, labels)) #
                    - tf.data.Dataset.from_generator(gen, output_types, output_shapes) #生成
                - from files
                    - tf.data.TextLineDataset(filenames)
                    - tf.data.FixedLengthRecordDataset(filenames)
                    - tf.data.TFRecordDataset(filenames)
            - tf.data.Iterator (Create an iterator to iterate through samples in Dataset)
                - iterator = dataset.make_one_shot_iterator() (Iterates through the dataset exactly once. No need to initialization.)
                - iterator = dataset.make_initializable_iterator (Iterates through the dataset as many times as we want. Need to initialize with each epoch.)
                    - 初始化是什么意思呢？
           
        - does tf.data really perform better?
            - speed
                - With placeholder: 9.05271519 seconds
                - With tf.data: 6.12285947 seconds
                - tf.data is implemented in C++ to avoid Python overhead
            - drawbacks
                - For prototyping, feed dict can be faster and easier to write (pythonic)
                - tf.data is tricky to use when you have complicated preprocessing or multiple data sources
                - NLP data is normally just a sequence of integers. In this case, transferring the data over to GPU is pretty quick, so the speedup of tf.data isn't that large
    
    - Queues
        - move your processing into C++ TensorFlow ops, and string them together with TensorFlow’s producer/consumer queues.
        - Uses TensorFlow ops to perform preprocessing, but driven by client threads, and complex.

- feedable tensor
