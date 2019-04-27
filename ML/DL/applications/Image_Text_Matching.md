
### Papers
1. [SCA, Stacked Cross Attention for Image-Text Matching. 2018 CVPR](https://arxiv.org/pdf/1803.08024.pdf)
    - [author's code](https://github.com/kuanghuei/SCAN)
    - saliency detector
        - A lightweight saliency detection model provides the visual saliency information as the guidance for the two attention modules
    - Saliency-weighted Visual Attention (SVA) module
        - leverage the advantage of the saliency information to improve discrimination of visual representations.
        - The visual attention module selectively attends to various local visual features via resorting to the lightweight saliency detector
        - take a step towards selectively attending to various words of the sentence.
    - Saliency-guided Textual Attention (STA) module
        - By fusing the visual information from SVA and textual information as a multi-modal guidance, STA learns discriminative textual representations that are highly sensitive to visual clues.
        - For the textual attention module, taking the intra-modality and inter-modality correlations into consideration, we merge the visual saliency, global visual and textual information effectively to generate multi-modal guidance for soft-attention mechanism, determining the importance of word-level textual features.
        - design a gated fusion unit to fuse multi-modal information effectively. 
    - points
        - an image usually has the capability to convey more detailed information than a sentence.
        - Unlike the above methods that explicitly aggregate local similarities to compute the global one
        - an asymmetrical architecture
    
2. [VSE, Improving Visual-Semantic Embeddings with Hard Negatives. 2017](https://arxiv.org/pdf/1707.05612.pdf)
    - [github code](https://github.com/fartashf/vsepp)
    - 利用batch里面hard negative做Max triplets hinge loss, 而不是Sum triplets hinge loss.

3. [DVSA, Deep Visual-Semantic Alignments for Generating Image Descriptions. 2015 CVPR]
    - [homepage](https://cs.stanford.edu/people/karpathy/deepimagesent/)
    
    
### Methods
- mapping whole images and full sentences to a common semantic vector space for image-text matching
- pairs of image regions and words 
    - Detect image regions at object/stuff level and simply aggregate the similarity of all possible pairs of image regions and words in sentence to infer the global image-text similarity.    

- global alignment based methods
- local alignment based methods
    - make the image-sentence matching more interpretable

### Questions
- heterogeneity gap
- CNN抽特征的问题
    - it is likely to get all the visual information in an image tangled with each other, which is unable to provide enough visual discrimination for image-sentence matching

### Metrics
- R@1

### Datasets
1. Flickr30K.
2. MS-COCO.0
