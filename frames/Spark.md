## 资料
- [RDD paper.NSDI 2012 Resilient Distributed Datasets: A Fault-Tolerant Abstraction for In-Memory Cluster Computing.](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf)
- [Offical document.](https://spark.apache.org/docs/latest/rdd-programming-guide.html)
- [Configuration](https://spark.apache.org/docs/latest/configuration.html)

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


## SparkSQL
- 特点
    - 上层SQL, 利用Spark执行引擎, 操作hive数据表
    - SQL on hadoop模式, 直接操作表.
    - 可以通过JDBC/ODBC连接其他数据源
    - 支持python, java, Scala, R语言
    - sparkSQL复用了hive的前端以及元数据

- 注意
    - sql 日期一定要加引号

## pyspark
- 环境变量
    - https://spark.apache.org/docs/latest/configuration.html#runtime-environment
    - PYSPARK_PYTHON 
        - 控制excutor的
    - PYSPARK_DRIVER_PYTHON
        - 控制driver的
    - spark.pyspark.driver.python 优先级比PYSPARK_DRIVER_PYTHON高
        Python binary executable to use for PySpark in driver. (default is spark.pyspark.python)
    - spark.pyspark.python	
        Python binary executable to use for PySpark in both driver and executors.
        
- 坑
    - pyspark 2.3 --archives ***/python.zip#python  此时引用还需要python.zip  spark.pyspark.python=./python.zip/python27/bin/python
    
    - TypeError: can't pickle SwigPyObject objects
        - 不能直接在partition外创建不可序列化的对象，比如faiss, tensorflow等, 只能在partition内部新建对象
        
- 内存优化
    - [官方文档](https://spark.apache.org/docs/latest/tuning.html#memory-management-overview)
    - 执行内存
        - 
    - 存储内存
        - 
    - While working with RDDs, avoid using groupByKeys. GroupBy keys tend to keep all values for a given key in memory. Keys having a very large value list that cannot be kept in memory will result in OOMs as they aren’t spilled to disk. One solution is to replace groupByKeys with reduceByKeys that does a map side combine and decreases the amount of data that is passed to the reducers.
        