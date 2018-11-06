## 环境变量
    - https://spark.apache.org/docs/latest/configuration.html#runtime-environment
    - PYSPARK_PYTHON 
        - 控制excutor的
    - PYSPARK_DRIVER_PYTHON
        - 控制driver的
    - spark.pyspark.driver.python
        Python binary executable to use for PySpark in driver. (default is spark.pyspark.python)
    - spark.pyspark.python	
        Python binary executable to use for PySpark in both driver and executors.
        
## 坑
    - pyspark 2.3 --archives ***/python.zip#python  此时引用还需要python.zip  spark.pyspark.python=./python.zip/python27/bin/python
    
    - TypeError: can't pickle SwigPyObject objects
        - 不能直接在partition外创建不可序列化的对象，比如faiss, tensorflow等, 只能在partition内部新建对象
        - 
