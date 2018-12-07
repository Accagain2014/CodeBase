## len not equal wc -l
    - pandas长度和wc -l 长度不一样
    - 很可能是英文引号原因，导致pandas读某一个值时，碰到了前引号，后引号在之后很多行后
    - eg:   a   "b  c   d
            a"  b   c   d
     
## 统计
    - 值统计
        - describe()
    - 频率统计
        - value_counts()
            - 只能统计列

## 设置
    - 设置浮点数输出，保留三位小数
        - pd.options.display.float_format = '{:.3f}'.format
    
        