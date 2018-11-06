## 基本点
    - /etc/profile 对所有用户有效
    - ~/.bashrc 对当前用户有效
    - export NAME=dir 临时有效，结束该shell，则无效
    - source filename 使变量生效
    - env 显示所有环境变量
    - set 显示本地定义的shell变量
    - unset 清除环境变量
    

## Python:
    - PYTHONPATH  
        - import不成功的话，查看该代码或者.so是否包含在PYTHONPATH环境内
        - 可以将需要的库/代码，放入python_dir/lib/python2.7
        
## 重要环境变量
   - LD_LIBRARY_PATH
        - C语言动态库, 通常以.so结尾
   - LIBRARY_PATH
        - C语言静态库, 通常以.a结尾
        
- 命令搜索库
    - PATH
    

    
