#!/usr/bin/env bash

for ((i=$1; i<=$2; i++))
do
	scp -r $1 sla${i}:$3 &
done