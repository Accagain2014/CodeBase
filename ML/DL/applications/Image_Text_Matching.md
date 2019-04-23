
### Papers
1. [SCA, Stacked Cross Attention for Image-Text Matching. 2018 CVPR](https://arxiv.org/pdf/1803.08024.pdf)
    - [author's code](https://github.com/kuanghuei/SCAN)
2. [VSE, Improving Visual-Semantic Embeddings with Hard Negatives. 2017](https://arxiv.org/pdf/1707.05612.pdf)
    - [github code](https://github.com/fartashf/vsepp)
    - 利用batch里面hard negative做Max triplets hinge loss, 而不是Sum triplets hinge loss.
3. [DVSA, Deep Visual-Semantic Alignments for Generating Image Descriptions. 2015 CVPR]
    - [homepage](https://cs.stanford.edu/people/karpathy/deepimagesent/)
    
    
### Methods
- mapping whole images and full sentences to a common semantic vector space for image-text matching
- pairs of image regions and words 
    - Detect image regions at object/stuff level and simply aggregate the similarity of all possible pairs of image regions and words in sentence to infer the global image-text similarity.    


### Metrics
- R@1

### Datasets
1. Flickr30K.
2. MS-COCO.0
