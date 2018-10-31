## 资料
- [RDD paper.NSDI 2012 Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing.](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf)
- [Offical document.](https://spark.apache.org/docs/latest/rdd-programming-guide.html)

## 特点
- RDDs(Resilient Distributed Datasets)
    - 创建
        - 从稳定的存储
        - 其他RDD(**transformations**: map, filter, join)
    - 实现
        - 不需要真正实物实现
        - 只需要保存创建过程，可以很容易重构
    - 操作
        - persistence and partitioning
        - Users can indicate which RDDs they will reuse and choose a storage strategy for them(eg in-memory storage).
        - They can also ask that an RDD's elements be partitioned across machines based on a key in each record.

## Spark(Programming Interface)
    - ![]()
    - Transformations(没有在集群做, 只是定义filter/map/join步骤)
        - lazy operations and define a new RDD
    - Actions()
        - launch a computation to return a value to the program or write data to external storage.
        - 给应用返回结果
        - 将数据导出给storage system
        - 举例
            - count/collect/save
        - persist
