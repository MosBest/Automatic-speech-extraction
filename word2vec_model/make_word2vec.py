from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

news_word2ve = Word2Vec(LineSentence('../data/news-sentences-xut.txt'), size=35, workers=8)
news_word2ve.save("./word2vermodel")
