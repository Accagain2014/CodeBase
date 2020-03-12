
1. coalesce
    - 当读取多个文件时, 比如大几万, 可能会导致失败率比较大，导致最终任务不能执行, 可以使用，将文档重新分片
    - 对文件进行合并
    - 与repatition区别, repartition对文件合并, 然后shuffle, 最后平均分
    
2. 可以通过拋异常, 查看worker上错误信息, 并打印. 
    - raise Exception("{}".format(data))
    
3. 处理str时, 注意ascii编码问题：
    - data.encode("utf-8") 

4. 注意(key, (value)), value[:5]是一个tuple, 使用使如果需要list, 则需要转成list

