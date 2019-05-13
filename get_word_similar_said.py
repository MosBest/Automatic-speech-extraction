from gensim.models import Word2Vec
from collections import defaultdict


def get_related_words(initial_words, model):
    """
    @initial_words
    @model
    """

    unseen = initial_words

    seen = defaultdict(int)

    max_size = 500

    while unseen and len(seen) < max_size:
        if len(seen) % 50 == 0:
            print('seen length : {}'.format(len(seen)))
        node = unseen.pop(0)

        new_expanding = [w for w, s in model.most_similar(node, topn=20)]

        unseen += new_expanding

        seen[node] += 1
    return seen


def get_words_said(model_path):
    model = Word2Vec.load(model_path)
    related_words = get_related_words(['说', '表示', '认为'], model)
    related_words = sorted(related_words.items(), key=lambda x: x[1], reverse=True)
    said = [i[0] for i in related_words if i[1] >= 9]
    return said


if __name__ == '__main__':
    path = "./word2vec_model/word2vermodel"
    get_words_said(path)
