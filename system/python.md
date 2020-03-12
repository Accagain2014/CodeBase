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


## python2 编码问题
- str
    - python 2: a Bytes string
    - python 3: an Unicode string

- unicode, u'value'
    - python 2: unicode
    - python 3: str

- Bytes string, b'value', "\xe5\x91\xa8\xe6\x9d\xb0\xe4\xbc\xa6"
    - python 2: str
    - python 3: bytes
 
 
- bytes.decode("utf-8") or str.decode("utf-8")
    - change bytes/str to unicode

- unicode.encode("utf-8")
    - change unicode to bytes/str
    
 
 
## python3 
- str.encode("utf-8")
    - change str type to bytes type.
    - '27岁少妇生孩子后变老' --->  b'27\xe5\xb2\x81\xe5\xb0\x91\xe5\xa6\x87\xe7\x94\x9f\xe5\xad\xa9\xe5\xad\x90\xe5\x90\x8e\xe5\x8f\x98\xe8\x80\x81'
- bytes.decode("utf-8")
    - change bytes type to str type
    - b'27\xe5\xb2\x81\xe5\xb0\x91\xe5\xa6\x87\xe7\x94\x9f\xe5\xad\xa9\xe5\xad\x90\xe5\x90\x8e\xe5\x8f\x98\xe8\x80\x81'  ---> '27岁少妇生孩子后变老' 
    
- str(bytes, 'utf-8')
    - change bytes type to str type