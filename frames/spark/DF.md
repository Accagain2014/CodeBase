#### 读取文件
    from pyspark.sql.types import StructType

    train_id_vec_path = 'HDFS directory '
    schema = StructType().add("***_id", StringType(), True).add("***_id", StringType(), True).add(\
        "***_id", StringType(), True).add("***_id", StringType(), True).add("***", StringType(), True)
    train_pd = spark.read.csv(HDFS+train_id_vec_path, header=None, sep='\t', schema=schema)
    train_pandas = train_pd.toPandas()
    
