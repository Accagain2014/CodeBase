Related Papers. 
----
- [Attention Is All You Need](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf)
    - 2017 NIPS. BERT之前， Transformer. Google Brain.
    - [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)
    - [tensor2tensor library](https://github.com/tensorflow/tensor2tensor)
    - [易懂的Kyubyong/transformer](https://github.com/Kyubyong/transformer)
    - 只依赖Attention的网络, 不依靠RNN和CNN。并行化更高，训练时间短。
    
   
- [Semi-supervised Sequence Learning](https://arxiv.org/abs/1511.01432)
    - 2015 NIPS. Andrew M. Dai, Quoc V. Le. Google.
    - 利用未标注的数据进行预训，提高文本分类的能力
    - 怎样利用未标注的数据？ pretrain
        - 语言模型的方式，预测序列中的下一个
        - 使用一个序列的autoencoder, reads the input sequence into a vector and predicts the input sequence again.
    - 利用未标注数据学习到的权重，给监督学习算法初始化参数
    
    
- [Improving Language Understanding by Generative Pre-Training](https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/language-unsupervised/language_understanding_paper.pdf)
    - OpenAI GPT (Radford et al., 2018)
    - [blog](https://blog.openai.com/language-unsupervised/)
    - [code](https://github.com/openai/finetune-transformer-lm)
    

- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)
   - 2018 . Google.
   - (tensorflow version)[https://github.com/google-research/bert]
   - 双向transformer + finetune

- Transfer Learning [迁移学习]
    - [cs 231n Transfer Learning](http://cs231n.github.io/transfer-learning/)
    - [Learning without Forgetting](http://zli115.web.engr.illinois.edu/wp-content/uploads/2016/10/0479.pdf)
    - Language model pre-training
        - feature-based. eg: ELMo (Peters et al. 2018)
        - fine-tuning. eg: OpenAI GPT(Generative Pre-trained Transformer) (Radford et al. 2018)
    


- [GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding](https://www.nyu.edu/projects/bowman/glue.pdf)
    - Wang et al. 2018
    - [glue-benchmark](https://gluebenchmark.com/leaderboard)


    
- MLM

- WordPiece tokenization


## squad
- 2.0 [Know What You Don’t Know: Unanswerable Questions for SQuAD](https://arxiv.org/pdf/1806.03822.pdf)


## Terms
- NLI: Natural Language Inference
- QA:  Question Answering
- GLUE: General Language Understanding Evaluation benchmark
 