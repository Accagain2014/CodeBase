## 基本操作



## 具体例子
1. 新建一个bare仓库，并关联;
```angular2html
    

```

2. 本地文件有修改，远程库也有修改，拉取远程的合并；
```angular2html
    git add .
    git commit -m 'local update'
    git pull
    # fix local conflict
    git add .
    git commit -m 'local update'
    git push orgin master
```