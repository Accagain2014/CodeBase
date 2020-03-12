#!/usr/bin/env bash


sort -t $'\t' -k2,2 -n -r
    # -t 分隔符; -k 指定列; -n 按数值排序; -r 逆序


cat baidu_sousuo_综艺.filter | awk '{ print length, $0 }' | sort -n | cut -d" " -f2- > baidu_sousuo_综艺.filter.sort

head -n 10000 ${f} | awk '{ print length, $0 }' | sort -n | cut -d" " -f2- > ../${f}