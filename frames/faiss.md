## 基本属性
    - 没有分布式版本，很少在spark/hadoop中跑
    - 支持GPU/CPU

 
## faiss gpu usage
    - on cpu
        - https://github.com/facebookresearch/faiss/blob/master/tutorial/python/4-GPU.py
    - on gpu
        - https://github.com/facebookresearch/faiss/wiki/Running-on-GPUs
        
        
## 功能
    - 支持write_index, save_index
    - 只支持np.float32建索引


##  KNN 


##  clustering parameters
struct ClusteringParameters {
    int niter;          ///< clustering iterations
    int nredo;          ///< redo clustering this many times and keep best

    bool verbose;
    bool spherical;     ///< do we want normalized centroids?
    bool update_index;  ///< update index after each iteration?
    bool frozen_centroids;  ///< use the centroids provided as input and do not change them during iterations

    int min_points_per_centroid; ///< otherwise you get a warning
    int max_points_per_centroid;  ///< to limit size of dataset

    int seed; ///< seed for the random number generator
}

ClusteringParameters::ClusteringParameters ():
    niter(25),
    nredo(1),
    verbose(false), spherical(false),
    update_index(false),
    frozen_centroids(false),
    min_points_per_centroid(39),
    max_points_per_centroid(256),
    seed(1234)
{}
// 39 corresponds to 10000 / 256 -> to avoid warnings on PQ tests with randu10k