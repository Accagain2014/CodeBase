#!/usr/bin/env bash

# $(NF) 表示最后一个
# $0 表示所有


# example 1: 输出\t分割的文件的第一列
awk 'BEGIN {OFS="\t"} {print $1}' filename
awk -F"\t" '{print $1}'

#