Why Tensorflow?
> **Flexibility[for research] + Scalability[for production]**  
> For a framework to be useful in production, it needs to be efficient, scalable, and maintainable. For research, the framework needs to have flexible operations that can be combined in novel ways. Alternative frameworks are either flexible enough for research but less scalable, such as Chainer and PyTorch, or scalable but less flexible, such as Caffe and MXNet. TensorFlow are both flexible and scalable, allowing users to streamline from research into production.

以矩阵的方式理解函数：

- 基本思想

- 基本概念
    - 静态/动态shape
    
    
- 矩阵操作函数
    - tf.gather
        - 对第axis维进行切片, 并根据indices进行汇聚
        - 当indices为标量/vector时比较好理解，表示从axis维取相应数据，形成新的数据
        - 当indices是矩阵时怎么理解？ 把最后一维当成是vector, 然后把结果依次加入到最后的矩阵里, 对axis=0可以这样理解
        - 当axis为非0时，理解有点问题, 再看一看
    - tf.gather_nd  
        - 按照indices[-1]值, 对params从第0维开始, 依次向里索引, 然后再包上indices[0: -1]维度
    
    
    - tf.stack
    - tf.concat
        - 对指定的axis进行拼接
    - tf.slice
        - 对连续的区间，进行裁剪
        
    - tf.tile(input, multiples)
        - 对input[i]复制multiples[i]次
        - This operation creates a new tensor by replicating input multiples times. The output tensor's i'th dimension has input.dims(i) * multiples[i] elements, and the values of input are replicated multiples[i] times along the 'i'th dimension. 
    
    - tf.scatter
        - 和gather相逆, 根据索引填充
        

- 矩阵运算
    - tf.matmul(A, B)
        - A, B的最后两维保证矩阵乘法可以进行，高维保持形状一样，最后一维更改，A[a1, a2, ..., an] * B[a1, a2, ..., an, bn] = C[a1, a2, ..., an-1, bn]

- 集成层
    - tf.layers.dense(inputs, units)
        - outputs = activation(inputs * kernel + bias) 
        - 自动根据输入构造W, 按units个数，最终输出网络结果

- loss设计
    - rank loss: max(0, s(N) - s(P) + e)
        - [batch_size, num_pos] => expand_dims [batch_size, num_pos, 1] => tiles [batch_size, num_pos, num_neg]
        - [batch_size, num_neg] => expand_dims [batch_size, 1, num_neg] => tiles [batch_size, num_pos, num_neg]
        - tf.maximum(0.0, [batch_size, num_pos, num_neg] - [batch_size, num_pos, num_neg] + e)
    
    