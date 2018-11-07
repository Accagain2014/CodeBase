#!/usr/bin/env bash


for ((day=$1; day<=$2; day++))
do
    date=`date -d "${day} days ago" "+%Y-%m-%d"`
    echo $date
    # handle file
done
