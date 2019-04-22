
### Start by Jupyter or Ipython
export PYSPARK_PYTHON=miniconda2/bin/python               
export PYSPARK_DRIVER_PYTHON=miniconda2/bin/python        
export PYSPARK_DRIVER_PYTHON=miniconda2/bin/ipython       
export SPARK_HOME=/usr/bin/hadoop/software/spark/                               
#export PYSPARK_DRIVER_PYTHON_OPTS="notebook"     是否使用jupyter                              
alias pyspark=/usr/bin/hadoop/software/spark/bin/pyspark                        
export PATH=miniconda2/bin:$PATH
    
    PYSPARK_PYTHON: slave执行路径, 必需设置这个环境变量, 在conf spark.pyspark.python里设置没用
    PYSPARK_DRIVER_PYTHON: driver执行路径, 如果在client模式【也即driver在本地】, 指向本地目录
    
    pyspark  \
        --master yarn \
        --queue **** \
        --driver-memory 10G \
        --executor-memory 10G \
         --conf spark.driver.maxResultSize=10g \
         --archives hdfs:**/tools/python27.zip#python27 \ #python27重命名
         --conf spark.pyspark.python=./python27/python27/bin/python \ #python27新的名字, 解压出来一层python27目录
         --conf spark.pyspark.driver.python=local:***/anaconda2/bin/ipython \
         --deploy-mode client \ # driver在本地
         --verbose \
         --conf spark.local.dir=local:/***/chenmaosen/tmp/
    
    from pyspark import SparkContext, SparkConf
    sc: SparkContext
    sqlCtx: HiveContext
    sqlContext: HiveContext
    
 
### Submit to cloud:
HDFS_DIR="hdfs:"
HOME_DIR="/home/***"
export PATH=miniconda2/bin:$PATH

export PYSPARK_PYTHON=./miniconda2/miniconda2/bin/python    # 指定slave python环境, 和参数效果一样，但得根据系统环境, 优先用哪一个不确定, 得试一试 --conf spark.pyspark.python
export PYSPARK_DRIVER_PYTHON=./miniconda2/miniconda2/bin/ipython    # 指定driver python环境, 和参数效果一样，但得根据系统环境, 优先用哪一个不确定, 得试一试 --conf spark.pyspark.driver.python=
export SPARK_HOME=/usr/bin/hadoop/software/spark


SPARK_SUBMIT=$SPARK_HOME/bin/spark-submit
$SPARK_SUBMIT \
    --master yarn \
    --deploy-mode client \
    --queue  ***.*** \
    --archives ${hdfs_python}#python27 \
    --py-files $project \
    --driver-memory 60G \
    --executor-memory 10G \
    --num-executors 3000 \
    --conf spark.local.dir=$tmp_dir \
    --conf spark.memory.fraction=0.3 \
    --conf spark.memory.storageFraction=0.5 \
    --conf spark.default.parallelism=1000 \    # 默认并行数量, 当文件很多时，读文件, 增大有利于提升速度
    --conf spark.sql.shuffle.partitions=1000 \  
    --conf spark.dynamicAllocation.maxExecutors=1000 \
    --conf spark.driver.maxResultSize=10g \
    --verbose \
    **.py --arg_key --arg_value



