    
### Papers for image-text matching
1. [DVSA, Deep Visual-Semantic Alignments for Generating Image Descriptions. 2015 CVPR]
    - [homepage](https://cs.stanford.edu/people/karpathy/deepimagesent/)
2. [Learning Deep Structure-Preserving Image-Text Embeddings. 2016 CVPR](https://zpascal.net/cvpr2016/Wang_Learning_Deep_Structure-Preserving_CVPR_2016_paper.pdf)
3. [What value do explicit high level concepts have in vision to language problems? In CVPR, 2016.]
4. [VSE, Improving Visual-Semantic Embeddings with Hard Negatives. 2017](https://arxiv.org/pdf/1707.05612.pdf)
    - [github code](https://github.com/fartashf/vsepp)
    - 利用batch里面hard negative做Max triplets hinge loss, 而不是Sum triplets hinge loss.
5. [SCA, Stacked Cross Attention for Image-Text Matching. 2018 ECCV](https://arxiv.org/pdf/1803.08024.pdf)
    - [author's code](https://github.com/kuanghuei/SCAN)
    - present Stacked Cross Attention to discover the full latent alignments.
    - Image-text matching with bottom-up attention.
    - 论文有点扯
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
6. [SCO, Learning Semantic Concepts and Order for Image and Sentence Matching. 2018 CVPR](http://openaccess.thecvf.com/content_cvpr_2018/papers/Huang_Learning_Semantic_Concepts_CVPR_2018_paper.pdf)
    - improving the image representation by learning semantic concepts and then organizing them in a correct semantic order.
    - model components: multi-regional multi-label CNN, gated fusion unit, and joint matching and generation learning
7. [Gen-XRN, Look, Imagine and Match: Improving Textual-Visual Cross-Modal Retrieval with Generative Models. 2018 CVPR](http://openaccess.thecvf.com/content_cvpr_2018/papers/Gu_Look_Imagine_and_CVPR_2018_paper.pdf)
    - incorporate the image-to-text and the text-to-image generative models into the conventional cross-modal feature embedding.
    - learn both the high-level abstract representation and the local grounded representation of multi-modal data in a maxmargin learning-to-rank framework.
8. [SGAN, Saliency-Guided Attention Network for Image-Sentence Matching. 2019](https://arxiv.org/pdf/1904.09471.pdf)


### Papers for text_to_image generation
1. [MirrorGAN: Learning Text-to-image Generation by Redescription. 2019 CVPR](https://arxiv.org/pdf/1903.05854.pdf)
2. [StoryGAN: A Sequential Conditional GAN for Story Visualization. 2019 CVPR](https://arxiv.org/pdf/1812.02784.pdf)
3. [Object-driven Text-to-Image Synthesis via Adversarial Training. 2019 CVPR]()


### Questions
1. the representation of pixel-level image usually lacks of high-level semantic information as in its matched sentence.


### Methods
- mapping whole images and full sentences to a common semantic vector space for image-text matching
    - As a result, some primary foreground concepts tend to be dominant, while other secondary background ones will probably be ignored,
    - global common space
    - shown great potential in learning discriminative cross-modal representations
    - computation efficiency at the test stage
    - do not consider the latent vision-language correspondence at the level of image regions and words.
    
- Pairwise similarity learning
    - designing a similarity network which predicts the matching score for image-text pairs. 
    - maximize the alignments between image regions and textual fragments.
    - the attribute learning frameworks (concepts)
    - pairs of image regions and words 
        - Detect image regions at object/stuff level and simply aggregate the similarity of all possible pairs of image regions and words in sentence to infer the global image-text similarity.    
    - local common space
    
- Image Captioning Based
    - generate a grammatically-complete sentence.

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
| Corpus | Task | #Train | #Dev | #Test | #Label | Metrics |  Source | 
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Flickr30K | Text_Image_Matching | 28k | 1k | 1k | 2 | R@K | Flickr website |
| MSCOCO | Text_Image_Matching | 82.7k | 4k | 1k/5k | 2 | R@K |  | 


### Terms
1. semantic concepts and order
    - order指的是什么意思呢？, 次序，语义次序
2. visual-semantic

### Related areas
1. image-sentence cross-modal retrieval
    - image annotation
    - text-based image search
2. visual question answering(VQA) 
3. image captioning