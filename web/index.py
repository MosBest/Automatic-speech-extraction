from bottle import Bottle, static_file, get
from bottle import template
from bottle import request
import json
import work

def del_sentences(string):
    path = "../word2vec_model/word2vermodel"
    said = work.get_words_said(path)

    ltp_model_path = '/home/zhaodao/下载/model/'
    sentences = work.split_sentences(string)
    sents = work.split_words(sentences)
    postags = work.get_word_pos(ltp_model_path, sents)
    contents = work.dependency_parsing(ltp_model_path, sents, postags, said)
    contents_dict = {}
    for indx, ones in enumerate(contents):
        contents_dict[str(indx)] = [ones[0], ones[1], ones[2]]
    print(contents_dict)
    return contents_dict

string1 = """
今天看到了微博热搜“人造奶”，非常好奇到底什么是人造奶？要知道现代世界科技发达，很多东西都能人造形成，就比如割的双眼皮，比如种的假酒窝等等，这些人造的东西真的是层出不穷，当然每个人都有自己选择的自由，但是今天出现的这个人造奶着实也是让人眼前一亮，也就是说，不需要奶牛的牛奶，如果是你你会喝吗？


据悉人造肉公司刚刚在美国上市大火，除了人造肉之外，人造奶也来了，而且在5月7日的时候，全球经济研究网站MishTalk的专栏作家Mike Shedlock在文章中就介绍了人造奶，什么是人造奶呢？就是一种更环保、更健康、更烧钱的奶，也就是说根本不需要奶牛就可以实现，听起来就跟我们从小喝的豆浆一样，而关于人造奶各路网友们也是热议不断，大多数的网友都在替奶牛担心，担心奶牛从此以后就失业了，也是非常的有意思。

当然如果人造奶大量的走向市场，如果是你你会选择喝吗？对于这个问题网友们也是有自己的看法，有人说肯定不会喝的，我感觉人造奶，人造肉都不太卫生都会对身体产生一定的危害，可能人造肉，人造奶的味道也不会好到哪里去，东西还是大自然的好，既健康又美味；也有人说这就相当于你会尝试方便面一样，明知道方便面有各种添加剂其营养价值低，但人们还是喜欢吃喜欢调料的味道。最主要的是给人们提供了方便。人造奶和人造肉的营养价值再高，但其有添加剂成分，可能会少吃吧。

每个人站在不同的角度也都给出了自己的看法，其实个人认为很多东西都是纯天然的最好，而对于人造奶这样的市场，大家觉得怎么样呢？你会选择喝人造奶吗？
"""

#contents_dict = del_sentences(string)

root = Bottle()

@root.route('/', method=['GET', 'POST'])
@root.route('/<name>', method=['GET', 'POST'])
def index(name={"1":[1,2,3]}):
    print(request.method)
    if request.method == 'GET':
        print("string2")
        return template('index.html', name=name)
    else:
        print("string1")
        import chardet

        string = request.forms.getunicode('string')
        print("string", string)
        string = string.encode("utf-8")
        print("string", string)
        contents_dict = del_sentences(string)
        print("contents_dict", contents_dict)
        contents_dict = json.dumps(contents_dict)
        print(contents_dict)
        return template('index.html', name=contents_dict)

# Static Routes
@root.route("/static/css/<filepath:re:.*\.css>", method=['GET', 'POST'])
def css(filepath):
    return static_file(filepath, root="static/css")

@root.route("/static/font/<filepath:re:.*\.(eot|otf|svg|ttf|woff|woff2?)>", method=['GET', 'POST'])
def font(filepath):
    return static_file(filepath, root="static/font")

@root.route("/static/img/<filepath:re:.*\.(jpg|png|gif|ico|svg)>", method=['GET', 'POST'])
def img(filepath):
    return static_file(filepath, root="static/img")

@root.route("/static/js/<filepath:re:.*\.js>", method=['GET', 'POST'])
def js(filepath):
    return static_file(filepath, root="static/js")

root.run(host='localhost', port=8091)
