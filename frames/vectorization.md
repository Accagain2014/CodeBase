##向量化操作总结
1. 怎样将两个数组，按值索引，进行平铺填充.
```
例如 
    s = [1, 2, 1], e = [2, 3, 2] => 
        [
            [0, 1, 1, 0], 
            [0, 0, 1, 1], 
            [0, 1, 1, 0]
        ]
代码
    start_label = tf.constant(np.array([0, 2, 3]))
    start_label = tf.sequence_mask(start_label, 5, dtype=tf.int32) # not include the index

    end_label = tf.constant(np.array([2, 4, 3]))
    end_label = tf.sequence_mask(end_label+1, 5, dtype=tf.int32)
    
    res = end_label - start_label
    
res:
array([[1, 1, 1, 0, 0],
       [0, 1, 1, 1, 1],
       [0, 0, 1, 1, 0]], dtype=int32)]
``` 

2. 给一个矩阵，怎样得到axis轴，索引[i, j]特征的avg.
```
例如
    input = [
        [1, 2, 3],
        [3, 2, 4],
        [2, 4, 1],
        [6, 7, 8],
    ], 
    indices = [2, 4] 
    => (input[2] + input[3] + input[4]) / 3.0
    
   
```

3. 给定矩阵和索引， 给相应索引赋值，
```
例如
    input = [
        [1, 2, 3],
        [3, 2, 4],
        [2, 4, 1],
        [6, 7, 8],
    ], 
    indices = [1, 1, 2, 2]    
    => [
        [0, 1, 0], 
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 1]
    ]
    
    用两个sequence_mask可以解决
```