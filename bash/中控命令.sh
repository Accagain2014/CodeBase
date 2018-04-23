#!/usr/bin/env bash

for ((i=$1; i<=$2; i++))
do
	ssh sla${i} "$3"
done


# 删除最后一行 sh command.sh 19 32 'sed -i "\$ d" ~/.bashrc'
# eg sh command.sh 19 34 'echo export PATH=/home/ada/chenmaosen/phantomjs-1.9.7-linux-x86_64/bin:/home/ada/chenmaosen/python3/bin:\$PATH >> ~/.bashrc ; source ~/.bashrc'

# 杀死包含phantomjs的所有进程
#   kill -9 `ps -aux | grep phantomjs | awk '{split($0,numbers," "); print numbers[2]}'`
#   killall phantomjs
#   sh command.sh 19 34 "kill -9 `ps -aux | grep phantomjs | awk '{split($0,numbers,\" \"); print numbers[2]}'`"
