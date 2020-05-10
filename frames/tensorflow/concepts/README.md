## Resources
- [Stanford CS 20: Tensorflow for Deep Learning Research](https://web.stanford.edu/class/cs20si/)
- [Kyubyong/tensorflow-exercises, equal with numpy](https://github.com/Kyubyong/tensorflow-exercises)
- [TensorFlow’s official sample models](https://github.com/tensorflow/models)
- [TensorFlow Tutorials](https://github.com/Hvass-Labs/TensorFlow-Tutorials)
- [Distributed TensorFlow](https://github.com/tensorflow/examples/blob/master/community/en/docs/deploy/distributed.md)


## Introduction
- Created by Google, 2015. 一种实现开源了，内部还有一个版本。 in both production and research. 

- Flexibility
    - can be combined in novel ways. 
    - eg: Chainer and PyTorch.

- Scalability
    - eg: Caffe and MXNet.

- 图定义和计算分离【非eager模式】
    - 第一步：构建图
    - 第二步：用session执行图上的操作
    

## Useful Points
- TensorFlow presents you with a declarative programming model because the specification of your computation (i.e., the creation of a Graph) is separated from the execution of it (i.e., running parts of the graph with a Session).
    - 问题？ TF 2.0, 支持Eager Execution, 建图和计算没有分离，是怎样做到速度跟上呢？
