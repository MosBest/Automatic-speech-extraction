# 快且精确的寻找similar embedding	
一个词的meaning 由　它的内容　和它周围的词决定。

功能：
同义词提取
在不同语言中　对其两个句子的单词
类比推断问题
寻找一个问题的解决文档

当我们想研发一个实时的问题扩展系统在搜索引擎上，那么这个项目和existing wor的关键不同是　embeddings 不在是高维向量，而是低维向量.

在　approximate similarity search 中有三种 索引　方法：
1. 基于哈希　索引 : 简单，易于处理稀疏和密集向量，多用于　nlp.
通过使用hash函数对高维空间进行降维,　从而使得我们可以在低维的空间中efficiently search。
算法1: Locality-sensitive hashing(LSH): 它通过使用多个哈希函数将相似的向量映射到具有高概率的相同哈希值。

2. 基于树　索引: 多用于图像索引
3. 基于图　索引: 多用于图像索引

本篇论文　做出以下的　贡献：
１．we focus on neu-ral word embeddings learned by a recently devel-oped skip-gram model (Mikolov, 2013)
2. show
that a graph-based search method clearly performs better than the best one reported in the Gorman and Curran study from different aspects
3. report the useful facts that normalizing vectors can achieve an effective search with cosine similarity, the search performance is more strongly related to a learning model of embeddings than its training data, the distribution shape of embeddings is a key factor relating to the search performance, and the final performance of a target application can be far different from the search performance.


In this paper, we focus on approximation of k-nearest neighbors and are not concerned about the hash-based indexing algorithms

they are basically designed for finding (not k-nearest) neighbors within a fixed radius of a given point, i.e., a 	so-called radius search.

使用　基于树方法的　FLANN, 和　基于图方法的 NGT。 再将FLANN，NGT 和　SASH　进行比较.
由于LSH广泛的应用于　nlp中，所以我们也用LSH做一下比较。我们使用E2LSH包，因为它对LSH算法做了实现。

目标：
给定一个向量，如何　快　且　精确的找到一个词的近似向量。
将这个问题定义为k-nearest neighbors。
定义N(X,d)为测量空间。
定义 metric 为d, vector x属于　X，的k_n_n集合为　N_k(x, d)

我们的目标就是　在给定vector x 下，近似得到　N_k(x, d).

定义　Ａ：表示近似搜索方法
定义：　评估方法Ｐ＠K 表示　方法Ａ得到的精度。

Ｐ＠K　定义为　|N_k(x, d) ∩ Ñ_k(x, A)| / k

评估方法　Ｐ＠K 　在信息检索中被广泛的使用。

基本设置：
使用　2015年2月的英文语料库（进行了数据预处理　Mahoney, 2011, Mikolov 2013） 训练200维的word embeddings 。

We used the　skip-gram learning model with hierarchical soft-max training in the word2vec tool, where the window size is 5, and the down-sampling　parameter is　0.001.

normalizing　them