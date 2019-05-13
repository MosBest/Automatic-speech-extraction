import os
from urils import deal
from get_word_similar_said import get_words_said

def split_sentences(string):
    from pyltp import SentenceSplitter
    sents = SentenceSplitter.split(string)
    sentences = [s for s in sents if len(s) != 0]
    return sentences


def split_words(sentences):
    sents = [deal(s) for s in sentences]
    return sents


def get_word_pos(ltp_model_path, sents):
    model_path = ltp_model_path
    pos_model_path = os.path.join(model_path, 'pos.model')
    from pyltp import Postagger
    postagger = Postagger()
    postagger.load(pos_model_path)
    postags = [postagger.postag(words.split()) for words in sents]
    postags = [list(w) for w in postags]

    postagger.release()
    return postags


def dependency_parsing(ltp_model_path, sents, postags, said):

    LTP_DATA_DIR = ltp_model_path # ltp模型目录的路径
    par_model_path = os.path.join(LTP_DATA_DIR, 'parser.model')  # 依存句法分析模型路径，模型名称为`parser.model`

    from pyltp import Parser
    parser = Parser()  # 初始化实例
    parser.load(par_model_path)  # 加载模型

    contents = []
    for index in range(len(sents)):
        wo = sents[index].split()

        po = postags[index]

        arcs = parser.parse(wo, po)  # 句法分析

        arcs = [(arc.head, arc.relation) for arc in arcs]

        arcs = [(i, arc) for i, arc in enumerate(arcs) if arc[1] == 'SBV']
        for arc in arcs:
            verb = arc[1][0]
            subject = arc[0]
            if wo[verb - 1] not in said:
                continue

            contents.append((wo[subject], wo[verb - 1], ''.join(wo[verb:])))
    # parser.release()  # 释放模型
    return contents


if __name__ == '__main__':
    string = """
    今天看到了微博热搜“人造奶”，非常好奇到底什么是人造奶？要知道现代世界科技发达，很多东西都能人造形成，就比如割的双眼皮，比如种的假酒窝等等，这些人造的东西真的是层出不穷，当然每个人都有自己选择的自由，但是今天出现的这个人造奶着实也是让人眼前一亮，也就是说，不需要奶牛的牛奶，如果是你你会喝吗？


    据悉人造肉公司刚刚在美国上市大火，除了人造肉之外，人造奶也来了，而且在5月7日的时候，全球经济研究网站MishTalk的专栏作家Mike Shedlock在文章中就介绍了人造奶，什么是人造奶呢？就是一种更环保、更健康、更烧钱的奶，也就是说根本不需要奶牛就可以实现，听起来就跟我们从小喝的豆浆一样，而关于人造奶各路网友们也是热议不断，大多数的网友都在替奶牛担心，担心奶牛从此以后就失业了，也是非常的有意思。

    当然如果人造奶大量的走向市场，如果是你你会选择喝吗？对于这个问题网友们也是有自己的看法，有人说肯定不会喝的，我感觉人造奶，人造肉都不太卫生都会对身体产生一定的危害，可能人造肉，人造奶的味道也不会好到哪里去，东西还是大自然的好，既健康又美味；也有人说这就相当于你会尝试方便面一样，明知道方便面有各种添加剂其营养价值低，但人们还是喜欢吃喜欢调料的味道。最主要的是给人们提供了方便。人造奶和人造肉的营养价值再高，但其有添加剂成分，可能会少吃吧。

    每个人站在不同的角度也都给出了自己的看法，其实个人认为很多东西都是纯天然的最好，而对于人造奶这样的市场，大家觉得怎么样呢？你会选择喝人造奶吗？
    """

    path = "./word2vec_model/word2vermodel"
    said = get_words_said(path)

    ltp_model_path = '/home/zhaodao/下载/model/'
    sentences = split_sentences(string)
    sents = split_words(sentences)
    postags = get_word_pos(ltp_model_path, sents)
    contents = dependency_parsing(ltp_model_path, sents, postags, said)
    print(contents)