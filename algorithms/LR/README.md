### 问题

1. 线性回归中，极大似然和最小二乘的等价性；

2. 逻辑回归中，交叉熵loss的推导(log_loss)，极大似然正例的对数几率？

3. 线性回归求导。

4. 不太适合类别特征。

5. 逻辑回归为什么用sigmod作为最后的转换
    - 正例的对数几率(西瓜书P58)
    - 可导
    - ln(y/(1-y)) = wx+b    =>  y = 1/(1+e^(-(wx+b))) 也叫逻辑函数logistic function
    - 交叉熵和逻辑回归的关系
    - logistic loss is sometimes called cross-entropy loss
