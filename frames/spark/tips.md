
1. coalesce
    - 当读取多个文件时, 比如大几万, 可能会导致失败率比较大，导致最终任务不能执行, 可以使用，将文档重新分片
    
2. 可以通过拋异常, 查看worker上错误信息, 并打印. 
    - raise Exception("{}".format(data))
    
3. 处理str时, 注意ascii编码问题：
    - data.encode("utf-8") 
