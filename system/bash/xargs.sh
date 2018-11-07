#!/usr/bin/env bash


hadoop fs -ls ${root_dir}/${day}* | xargs -n 1 | zgrep ${filter} | xargs -n 1  -P 24 -I {} hadoop fs -cat {} | zgrep ${uid} | zgrep c=**