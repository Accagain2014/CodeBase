#!/usr/bin/env python3
#coding=utf-8

'''
@Author : Accagain
@Time   : 2020/4/7 下午6:45
@File   : scope.py

@Cont
    
'''



- scope
    - 主要用于共享变量
    
    - name scope
        - Group nodes together with tf.name_scope(name)
        - 作用于操作
        
    - variable scope
        - Variable scope facilitates variable sharing
        - get_variable
            - If a variable with <name> already exists, reuse it, If not, initialize it with <shape> using <initializer>
            - scope.reuse_variables()
            
    - the two relations
        - tf.variable_scope implicitly creates a name scope
        
    - tf.get_variable()创建的变量名不受 name_scope 的影响，而且在未指定共享变量时，如果重名会报错；
    - tf.Variable()受name_scope和tf.variable_scope影响；
    - 当多个tf_variable_scope嵌套时，如果中间某层开启了reuse=True, 则内层自动全部共享，即使内层设置了reuse=False；
    - 在同一scope下，如果使用tf.get_variable()创建变量，且没有设置共享变量，重名时会报错；
    - ｀tf.variable_scope｀和｀tf.get_variable｀必须要搭配使用（全局scope除外），为share提供支持；
    - ｀tf.Variable｀可以单独使用，也可以搭配｀tf.name_scope｀使用，给变量分类命名，模块化；
    - 当多个tf_variable_scope嵌套时，如果中间某层开启了reuse=True, 则内层自动全部共享，即使内层设置了reuse=False；
    

