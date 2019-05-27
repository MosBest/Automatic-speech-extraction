import os
from data.urils import deal
from similar_said.get_word_similar_said import load_said


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
    ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 依存句法分析模型路径，模型名称为`parser.model`

    from pyltp import Parser, NamedEntityRecognizer
    recognizer = NamedEntityRecognizer() # 初始化实例
    recognizer.load(ner_model_path)  # 加载模型

    parser = Parser()  # 初始化实例
    parser.load(par_model_path)  # 加载模型

    contents = []
    for index in range(len(sents)):
        wo = sents[index].split()

        po = postags[index]

        netags = recognizer.recognize(wo, po)  # 命名实体识别
        # print("netags", list(netags))
        netags = list(netags)
        if ('S-Ns' not in netags) and ('S-Ni' not in netags) and ('S-Nh' not in netags):
            continue

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
    # recognizer.release()  # 释放模型
    return contents






def del_sentences(string):
    path = "./similar_said/"
    said = load_said(path + "similar_said.txt")

    ltp_model_path = './model/'
    sentences = split_sentences(string)
    sents = split_words(sentences)

    postags = get_word_pos(ltp_model_path, sents)

    contents = dependency_parsing(ltp_model_path, sents, postags, said)
    contents_dict = {}
    for indx, ones in enumerate(contents):
        contents_dict[str(indx)] = [ones[0], ones[1], ones[2]]

    return contents_dict


if __name__ == '__main__':
    string = """
    新华社阿布扎比5月27日电（记者苏小坡）阿联酋阿布扎比王储穆罕默德26日晚在首都阿布扎比会见来访的苏丹过渡军事委员会主席阿卜杜勒·法塔赫·布尔汉时表示，阿联酋将支持苏丹为维护国家安全和稳定所做出的努力，并呼吁各方通过对话实现民族和解。

据阿联酋通讯社报道，穆罕默德表示，相信苏丹有能力克服目前的困难，实现和平的政治过渡和民族和解。

布尔汉对阿联酋支持苏丹的立场表示感谢，并特别感谢阿联酋对苏丹提供的财政帮助。

4月21日，阿联酋和沙特宣布联合向苏丹提供30亿美元实物和现金援助。目前，阿联酋和沙特已提供5亿美元作为苏丹央行的存款。

4月11日，苏丹国防部长伊本·奥夫宣布推翻巴希尔政权，并成立过渡军事委员会，负责执掌国家事务。4月12日，奥夫宣布辞去其过渡军事委员会主席职务，由布尔汉接任。
    """
    print( del_sentences(string) )
