#!/usr/bin/env bash

# $(NF) 表示最后一个
# $0 表示所有


# example 1: 输出\t分割的文件的第一列
awk 'BEGIN {OFS="\t"} {print $1}' filename
awk -F"\t" '{print $1}'

# example 2: 统计第二列为空的行数，并输出该行
cat all_part.csv | awk -F"\t" '{if(!$2) {C++; print $0}} END {print C} '
# END表示最后输出, 否则每一行输出





### Tips
- 注意最后使用'{}', 而不是"{}"
