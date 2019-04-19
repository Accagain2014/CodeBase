#### 执行sql
    from pyspark.sql.functions import *
    from pyspark.sql.types import *
    
    sqlContext.sql('use db_name')
    sql = sqlContext.sql(sql)
    
