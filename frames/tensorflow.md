以矩阵的方式理解函数：

- 基本思想

- 基本概念
    - 静态/动态shape
    
    
- 矩阵操作函数
    - tf.gather
        - 对第axis维进行切片, 并根据indices进行汇聚
        - 当indices为标量/vector时比较好理解，表示从axis维取相应数据，形成新的数据
        - 当indices是矩阵时怎么理解？ 把最后一维当成是vector, 然后把结果依次加入到最后的矩阵里
    - tf.stack
    - tf.concat
        - 对指定的axis进行拼接
    - tf.slice
        - 对连续的区间，进行裁剪
        
    - tf.tile(input, multiples)
        - 对input[i]复制multiples[i]次
        - This operation creates a new tensor by replicating input multiples times. The output tensor's i'th dimension has input.dims(i) * multiples[i] elements, and the values of input are replicated multiples[i] times along the 'i'th dimension. 

- 矩阵运算
    - tf.matmul(A, B)
        - A, B的最后两维保证矩阵乘法可以进行，高维保持形状一样，A[a1, a2, ..., an] * B[a1, a2, ..., an, bn] = C[a1, a2, ..., an-1, bn]

- 集成层
    - tf.layers.dense(inputs, units)
        - outputs = activation(inputs * kernel + bias) 
        - 自动根据输入构造W, 按units个数，最终输出网络结果
        