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

4. 给定一个两个矩阵，一个是logits = [batch_size, num_pos+num_neg],
    另一个是labels = [batch_size, num_pos+num_neg], 其中0表示该样本是正例, 1表示该样本是负例
    计算rank_loss, 对每一个样本的正例，随机5个作为负样例, 然后计算max(0, log_neg - log_pos + margin)
    ```
    例如：
        logits = [
            [0.9, 0.2, 0.3],
            [0.4, 0.1, 0.5]
        ]
        lables = [
            [1, 1, 0],
            [1, 0, 0]
        ]
    
        res = max(0, random([0.3]) - 0.9 + margin) + max(0, random([0.3]) - 0.2 + margin)
              + max(0, random([0.1, 0.5]) - 0.4 + margin)
    
        妥协方案：
            先随机开始位置, 然后随机长度[0, 10]
        
    ```

5. 索引. 给定input = [batch_size, n1, n2], indices = [batch_size, n1, k], 对最后一维进行索引.
    - 采用tf.gather_nd, 通过构造indices.
    - 
    
6. 给定logits = [batch_size, N], 和labels = [batch_size, N] (多label预测), 计算topk召回和正确率
    ```
        logits = [
            [0.9, 0.2, 0.3],
            [0.4, 0.1, 0.5]
        ]
        lables = [
            [1, 1, 0],
            [1, 0, 0]
        ]
    
    top_1_recall = (1/2 + 0)/2 = 0.15, top_2_recall = (1/2 + 1/1)/2 = 0.75, top_3_recall = (2/2 + 1/1)/2 = 1
    top_1_precise = (1/1 + 0/1)/2 = 0.5, top_2_precise = (1/2 + 1/2)/2 = 0.5 top_3_precise = (2/3 + 1/3)/2 = 0.5
    ```
    
