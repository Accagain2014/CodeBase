## 问题
- list相关
    - 注意list index 如果有重复元素的话 得不到当前的
        - 可以用 for index, item in enumerate(list): 解决
    - 字符串直接相加，当长度很大时的很慢，可以用list append，然后再转换成字符串
    - xrange, python2 range(1, huge)时生成很大的list, 浪费时间

- 编码相关
    - 当文件中存在控制不可打印字符，不知道分隔符是什么的时候
        - 先输出unicode编码(x**)
        - 分析unicode编码情况，直接以unicode编码作为分隔符进行处理
        - 在控制台直接打开文件读取，输出unicode编码
 