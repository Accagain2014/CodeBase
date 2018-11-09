#!/usr/bin/env bash

files=(`$HADOOP fs -ls $HDFS$path | awk '{print $NF}' | sort -r`)
cnt=0
MaxFile=3
for file in "${files[@]:1}"
do
     echo ***:$file
     $HADOOP fs -test -e $HDFS$file
     if [[ $? -eq 0 ]]; then
 	((cnt++))
	if [[ $cnt -gt $MaxFile ]]; then
	   echo "remove file" $HDFS$file
	   #$HADOOP fs -rmr $HDFS$file
	fi
     fi
done
