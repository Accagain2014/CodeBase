#!/usr/bin/env bash

# 数组使用
array=(1 2 3 8 7 6) # 定义
echo ${array[0]} # 访问
echo ${#array[@]} # 数组长度
array[0]=2 # 修改
echo ${array[0]}

# IF
if [[ ${array[0]} -eq 1 && ${array[1]} -eq 2 ]]; then
    echo "Accept."
fi

# WHILE
cnt=0
while true ; do
    ((cnt++))
    echo $cnt
    if [[ $cnt -gt 10 ]]; then
        break
    fi
done

# FOR
queue_index=3
for ((cnt=0; cnt<$queue_index; cnt++))
do
  EXE_TASK[$cnt]=1
  echo ${EXE_TASK[@]}
done
l